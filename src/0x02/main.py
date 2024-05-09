from bcc import BPF

text = """
int kprobe__sys_sync(void *ctx) {
    bpf_trace_printk("Hello, World!\\n");
    return 0;
}
"""

print("Tracing sys_sync()… Ctrl-C to end.")
BPF(text=text).trace_print()