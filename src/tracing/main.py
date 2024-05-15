from bcc import BPF

b = BPF(src_file="./src/bpf.c")

b.attach_uprobe(name="/usr/lib/libfunc.so", sym="hello", fn_name="traceHello")

print("Tracing Hello...")

while True:
    try:
        print(b.trace_fields())
    except KeyboardInterrupt:
        exit()
