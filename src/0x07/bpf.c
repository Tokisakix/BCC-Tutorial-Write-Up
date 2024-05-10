#include <linux/sched.h>

// define output event structure in C
struct event_t {
    u32 pid;
    u64 ts;
    char comm[TASK_COMM_LEN];
};
BPF_PERF_OUTPUT(result);

int hello(struct pt_regs *ctx) {
    struct event_t event = {};

    event.pid = bpf_get_current_pid_tgid();
    event.ts = bpf_ktime_get_ns();
    bpf_get_current_comm(&event.comm, sizeof(event.comm));

    result.perf_submit(ctx, &event, sizeof(event));

    return 0;
}