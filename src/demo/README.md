# Uprobe Tracing Demo

这个 **Demo** 演示了 **eBPF** 如何追踪用户库函数的运行状态。

## Code

首先是 `func.c` 文件，里面有个 `void hello()` 函数，稍后我们将其编译成一个 `libfunc.so` 动态库。

```C
#include <stdio.h>

void hello() {
    printf("Hello!\n");
    return;
}
```

然后是 `main.c` 文件，这里仅声明不给出 `void hello()` 的实现，我们稍后在编译时将此程序与 `libfunc.so` 库动态链接。

```C
void hello();

int main() {
    hello();
    return 0;
}
```

接着是 `bpf.c` 文件，`traceHello()` 会被挂载到 `void hello()` 的入口。

```C
int traceHello(struct pt_regs *ctx) {
    bpf_trace_printk("Hello called\n");
    return 0;
}
```

最后是 `main.py` 文件，这个程序会监听 `/usr/lib/libfunc.so` 动态库里 `void hello()` 函数的运行情况。

```Python
from bcc import BPF

b = BPF(src_file="./src/bpf.c")

b.attach_uprobe(name="/usr/lib/libfunc.so", sym="hello", fn_name="traceHello")

print("Tracing Hello...")

while True:
    try:
        print(b.trace_fields())
    except KeyboardInterrupt:
        exit()

```

## Compile

首先编译源文件，生成 `libfunc.so` 动态库和 `main.out` 执行文件。

```Shell
cd demo
make
```

然后安装，将编译好的 `libfunc.so` 复制到库目录 `/usr/lib/libfunc.so` 下。

```Shell
make install
```

测试动态链接情况。

```Shell
ldd ./main.out

# 期望出现类似输出
# libfunc.so => /lib/libfunc.so (0x00007f315f002000)
```

测试运行 `main.out`。

```Shell
make run

# 期望出现类似输出
# Hello!
```

最后运行 BCC 程序，监听 `void hello()` 运行情况，注意 `make run` 指令需要新开一个窗口执行。

```Shell
sudo python main.py

make run
```

![img](asset/demo.jpg)