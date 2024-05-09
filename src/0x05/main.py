from __future__ import print_function
from bcc import BPF

# load BPF program
b = BPF(src_file="bpf.c")

b.attach_kprobe(event=b.get_syscall_fnname("sync"), fn_name="do_trace")
print("Tracing for quick sync's... Ctrl-C to end")

# format output
start = 0
while 1:
    (task, pid, cpu, flags, ts, ms) = b.trace_fields()
    if start == 0:
        start = ts
    ts = ts - start
    ms = str(ms, encoding="utf-8")
    (fast_count, slow_count) = ms.split(",")
    print(f"At time {ts:6.2f} s: syncs detected, {fast_count:>3s} fast {slow_count:>3s} slow")