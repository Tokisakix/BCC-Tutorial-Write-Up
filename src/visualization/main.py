from bcc import BPF
import json

funcs = ["func_a", "func_b", "func_c", "func_d"]
template = """
int start_[func_name](struct pt_regs *ctx) {
    u64 tid = bpf_get_current_pid_tgid();
    bpf_trace_printk("%d [func_name] start\\n", tid);
    return 0;
}

int end_[func_name](struct pt_regs *ctx) {
    u64 tid = bpf_get_current_pid_tgid();
    bpf_trace_printk("%d [func_name] end\\n", tid);
    return 0;
}
"""
text = "".join([template.replace("[func_name]", func_name) for func_name in funcs])
b = BPF(text=text)

for func_name in funcs:
    b.attach_uprobe(name="/usr/lib/libfunc.so", sym=func_name, fn_name=f"start_{func_name}")
    b.attach_uretprobe(name="/usr/lib/libfunc.so", sym=func_name, fn_name=f"end_{func_name}")

trace_data = []
func_start = {}

try:
    print("Tracing Func...")
    while True:
        try:
            (task, pid, cpu, flags, ts, msg) = b.trace_fields()
        except ValueError:
            continue
        tid, func_name, op = str(msg, encoding="utf-8").split(" ")
        func_key = f"{tid}_{func_name}"
        if op == "start":
            func_start[func_key] = ts
        elif op == "end":
            dur = ts - func_start[func_key]
            trace_data.append({
                "name": func_name,
                "cat": "func",
                "ph": "X",
                "ts": func_start[func_key] * 1_000_000,
                "pid": pid,
                "tid": int(tid),
                "dur": dur * 1_000_000,
                "args": {},
            })
except KeyboardInterrupt:
    print("\nEnd Tracing...")
    with open("trace.json", 'w', encoding='utf-8') as file:
        json.dump(trace_data, file, ensure_ascii=False, indent=4)
    exit()