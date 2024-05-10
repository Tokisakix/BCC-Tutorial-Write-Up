# BCC Tutorial Write Up

## BCC

BPF Compiler Collection (BCC) is a toolkit for creating efficient kernel tracing and manipulation programs, and includes several useful tools and examples. It makes use of extended BPF (Berkeley Packet Filters), formally known as eBPF, a new feature that was first added to Linux 3.15. Much of what BCC uses requires Linux 4.1 and above.

![logo](asset/logo2.png)

## Write Up

1. [Hello World](src/0x01/README.md)
2. [sys_sync()](src/0x02/README.md)
3. [hello_fields.py](src/0x03/README.md)
4. [sync_timing.py](src/0x04/README.md)
5. [sync_count.py](src/0x05/README.md)
6. [disksnoop.py](src/0x06/README.md)
7. [hello_perf_output.py](src/0x07/README.md)
8. [sync_perf_output.py](src/0x08/README.md)
9. [bitehist.py](src/0x09/README.md)
10. [disklatency.py](src/0x10/README.md)
11. [vfsreadlat.py](src/0x11/README.md)
12. [urandomread.py](src/0x12/README.md)
13. [disksnoop.py-fixed](src/0x13/README.md)
14. strlen_count.py
15. nodejs_http_server.py
16. task_switch.c
17. Further Study

## Reference

- [BCC Tutorial](https://github.com/iovisor/bcc/blob/master/docs/tutorial_bcc_python_developer.md)
- [BCC Reference](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md)