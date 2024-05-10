from __future__ import print_function
from bcc import BPF

REQ_WRITE = 1

# load BPF program
b = BPF(src_file="bpf.c")

if BPF.get_kprobe_functions(b'blk_start_request'):
    b.attach_kprobe(event="blk_start_request", fn_name="trace_start")
b.attach_kprobe(event="blk_mq_start_request", fn_name="trace_start")

if BPF.get_kprobe_functions(b'__blk_account_io_done'):
    b.attach_kprobe(event="__blk_account_io_done", fn_name="trace_completion")
else:
    b.attach_kprobe(event="blk_account_io_done", fn_name="trace_completion")

# header
print("%-18s %-2s %-7s %8s" % ("TIME(s)", "T", "BYTES", "LAT(ms)"))
start = 0

# format output
while 1:
    try:
        (task, pid, cpu, flags, ts, msg) = b.trace_fields()
        (bytes_s, bflags_s, us_s) = str(msg, encoding="utf-8").split()

        if start == 0:
            start = ts

        if int(bflags_s, 16) & REQ_WRITE:
            type_s = "W"
        elif bytes_s == "0":
            type_s = "M"
        else:
            type_s = "R"
        ms = float(int(us_s, 10)) / 1000

        print(f"{ts - start:<18.9f} {type_s:2s} {bytes_s:>5s} {ms:10.2f}")
    except KeyboardInterrupt:
        exit()