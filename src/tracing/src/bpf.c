int traceHello(struct pt_regs *ctx) {
    bpf_trace_printk("Hello called\n");
    return 0;
}