#include <uapi/linux/ptrace.h>
#include <linux/blk-mq.h>

BPF_HASH(start, struct request *, u64);

void trace_start(struct pt_regs *ctx, struct request *req) {
	u64 ts = bpf_ktime_get_ns();
	start.update(&req, &ts);
}

void trace_completion(struct pt_regs *ctx, struct request *req) {
	u64 *tsp, delta;

	tsp = start.lookup(&req);
	if (tsp != 0) {
		delta = bpf_ktime_get_ns() - *tsp;
		bpf_trace_printk("%d %x %d\n", req->__data_len, req->cmd_flags, delta / 1000);
		start.delete(&req);
	}
}