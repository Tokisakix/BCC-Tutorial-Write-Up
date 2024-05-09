#include <uapi/linux/ptrace.h>

BPF_HASH(last);

int do_trace(struct pt_regs *ctx) {
    u64 ts, *tsp, delta, key = 0;
    u64 k1 = 1, k2 = 2;
    u64 *n1, *n2, v1 = 0, v2 = 0;

    // attempt to read stored timestamp
    tsp = last.lookup(&key);
    n1 = last.lookup(&k1);
    n2 = last.lookup(&k2);
    if (tsp != 0 && n1 != 0 && n2 != 0) {
        delta = bpf_ktime_get_ns() - *tsp;
        v1 = (*n1);
        v2 = (*n2);
        if (delta < 1000000000) {
            v1 ++;
        } else {
            v2 ++;
        }
        bpf_trace_printk("%d,%d\n", v1, v2);
        last.delete(&key);
    }

    // update stored timestamp
    ts = bpf_ktime_get_ns();
    last.update(&key, &ts);
    last.update(&k1, &v1);
    last.update(&k2, &v2);
    return 0;
}