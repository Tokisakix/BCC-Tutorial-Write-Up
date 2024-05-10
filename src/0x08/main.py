from __future__ import print_function
from bcc import BPF

# load BPF program
b = BPF(src_file="bpf.c")

b.attach_kprobe(event=b.get_syscall_fnname("sync"), fn_name="do_trace")
print("Tracing for quick sync's... Ctrl-C to end")

# process event
start = 0
def print_event(cpu, data, size):
    global start
    event = b["result"].event(data)
    if start == 0:
            start = event.ts
    ts = (float(event.ts - start)) / 1000000000
    ms = event.ms / 1000000
    print(f"At time {ts:.2f} s: multiple syncs detected, last {ms:.2f} ms ago")

# loop with callback to print_event
b["result"].open_perf_buffer(print_event)
while 1:
    b.perf_buffer_poll()
