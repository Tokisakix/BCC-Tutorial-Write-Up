from bcc import BPF

# load BPF program
b = BPF(src_file = "bpf.c")
b.attach_kprobe(event="vfs_read", fn_name="do_entry")
b.attach_kretprobe(event="vfs_read", fn_name="do_return")

# header
print("Tracing... Hit Ctrl-C to end.")

# output
try:
    while(True):
        pass
except KeyboardInterrupt:
    pass

b["dist"].print_log2_hist("usecs")
b["dist"].clear()