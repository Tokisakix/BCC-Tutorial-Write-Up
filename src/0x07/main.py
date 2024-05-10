from bcc import BPF

b = BPF(src_file="bpf.c")
b.attach_kprobe(event=b.get_syscall_fnname("clone"), fn_name="hello")

print("%-18s %-16s %-6s %8s" % ("TIME(s)", "COMM", "PID", "MESSAGE"))

# process event
start = 0
def print_event(cpu, data, size):
    global start
    event = b["result"].event(data)
    if start == 0:
            start = event.ts
    time_s = (float(event.ts - start)) / 1000000000
    print("%-18.9f %-16s %-6d %s" % (time_s, str(event.comm, encoding="utf-8"), event.pid, "Hello, perf_output!"))

# loop with callback to print_event
b["result"].open_perf_buffer(print_event)
while 1:
    b.perf_buffer_poll()