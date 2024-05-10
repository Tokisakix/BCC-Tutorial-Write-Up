from bcc import BPF

# load BPF program
b = BPF(src_file="bpf.c")

# header
print("Tracing... Hit Ctrl-C to end.")

# trace until Ctrl-C
try:
    while(True):
        pass
except KeyboardInterrupt:
	pass

# output
b["dist"].print_log2_hist("kbytes")