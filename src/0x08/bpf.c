#include <uapi/linux/ptrace.h>

struct event_t {
    u64 ts;
    u64 ms;
};
BPF_PERF_OUTPUT(result);
BPF_HASH(last);

int do_trace(struct pt_regs *ctx) {
    u64 ts, *tsp, key = 0;

    // attempt to read stored timestamp
    tsp = last.lookup(&key);
    if (tsp != 0) {
        struct event_t event = {};
        event.ts = bpf_ktime_get_ns();
        event.ms = event.ts - *tsp;
        if (event.ms < 1000000000) {
            // output if time is less than 1 second
            result.perf_submit(ctx, &event, sizeof(event));
        }
        last.delete(&key);
    }

    // update stored timestamp
    ts = bpf_ktime_get_ns();
    last.update(&key, &ts);
    return 0;
}