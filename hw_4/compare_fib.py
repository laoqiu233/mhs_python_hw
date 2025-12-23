import time
from multiprocessing import Process
from threading import Thread

FIB_LIMIT = 100000
WORKERS = 10


def fib(n: int):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def test_threading():
    threads: list[Thread] = []
    for _ in range(WORKERS):
        t = Thread(target=fib, args=(FIB_LIMIT,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def test_multiprocessing():
    processes: list[Process] = []
    for _ in range(WORKERS):
        p = Process(target=fib, args=(FIB_LIMIT,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.time()
    test_threading()
    print("Threading time: ", time.time() - start)
    start = time.time()
    test_multiprocessing()
    print("Multiprocessing time: ", time.time() - start)
