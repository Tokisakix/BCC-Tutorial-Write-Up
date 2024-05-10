#include <uapi/linux/ptrace.h>
#include <linux/blkdev.h>

BPF_HISTOGRAM(dist);

int kprobe__blk_account_io_completion(struct pt_regs *ctx, struct request *req){
	dist.increment(bpf_log2l(req->__data_len / 1024));
	return 0;
}