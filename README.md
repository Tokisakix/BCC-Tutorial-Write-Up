# BCC Tutorial Write Up

## BCC

BPF Compiler Collection (BCC) is a toolkit for creating efficient kernel tracing and manipulation programs, and includes several useful tools and examples. It makes use of extended BPF (Berkeley Packet Filters), formally known as eBPF, a new feature that was first added to Linux 3.15. Much of what BCC uses requires Linux 4.1 and above.

![logo](asset/logo2.png)

## Write Up

1. [Hello World](src/0x01/README.md)
2. [sys_sync()](src/0x02/README.md)
3. hello_fields.py
4. sync_timing.py
5. sync_count.py
6. disksnoop.py
7. hello_perf_output.py
8. sync_perf_output.py
9. bitehist.py
10. disklatency.py
11. vfsreadlat.py
12. urandomread.py
13. disksnoop.py fixed
14. strlen_count.py
15. nodejs_http_server.py
16. task_switch.c
17. Further Study

## Reference

- [BCC Tutorial](https://github.com/iovisor/bcc/blob/master/docs/tutorial_bcc_python_developer.md)
- [BCC Reference](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md)