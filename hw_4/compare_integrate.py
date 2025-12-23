import math
import multiprocessing
import statistics
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def integrate(f, a, b, n_jobs=1, job_index=0, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(job_index, n_iter, n_jobs):
        acc += f(a + i * step) * step
    return acc


def work_item(worker_id: int, workers: int):
    return integrate(math.cos, 0, math.pi / 2, workers, worker_id, 10000000)


MAX_WORKERS = multiprocessing.cpu_count() * 2
DELTA = 0.0001


def test_thread_pool(single_thread_result: float, n_iters: int) -> list[tuple[int, list[float]]]:
    results = []

    for workers in range(1, MAX_WORKERS + 1):
        timings = []
        for _ in range(n_iters):
            start = time.time()
            result = 0
            with ThreadPoolExecutor(workers) as pool:
                workers_result = pool.map(work_item, range(workers), [workers] * workers)
                result = sum(workers_result)
            if abs(result - single_thread_result) > DELTA:
                raise ValueError(f"Wrong answer on thread pool with {workers} workers")
            total = time.time() - start
            timings.append(total)
        results.append((workers, timings))

    return results


def test_process_pool(single_thread_result: float, n_iters: int) -> list[tuple[int, list[float]]]:
    results = []

    for workers in range(1, MAX_WORKERS + 1):
        timings = []
        for _ in range(n_iters):
            start = time.time()
            result = 0
            with ProcessPoolExecutor(workers) as pool:
                workers_result = pool.map(work_item, range(workers), [workers] * workers)
                result = sum(workers_result)
            if abs(result - single_thread_result) > DELTA:
                raise ValueError(f"Wrong answer on process pool with {workers} workers")
            total = time.time() - start
            timings.append(total)
        results.append((workers, timings))

    return results


if __name__ == "__main__":
    start = time.time()
    single_thread_result = work_item(0, 1)
    total = time.time() - start

    print(f"Single thread result: {single_thread_result} | Time taken: {total}")

    print("Running tasks on thread pool")
    start = time.time()
    threads_results = test_thread_pool(single_thread_result, 5)
    total = time.time() - start
    print(f"Finished thread pool test in {total} seconds")

    print("Running tasks on process pool")
    start = time.time()
    processes_results = test_process_pool(single_thread_result, 10)
    total = time.time() - start
    print(f"Finished process pool test in {total} seconds")

    print("Thread pool results:")
    print("-" * 80)
    print(f"{'Workers':<10} {'Mean (s)':<12} {'Min (s)':<12} {'Median (s)':<12} {'Max (s)':<12}")
    print("-" * 80)

    for workers, timings in threads_results:
        mean_time = statistics.mean(timings)
        median_time = statistics.median(timings)
        min_time = min(timings)
        max_time = max(timings)
        print(
            f"{workers:<10} {mean_time:<12.4f} {min_time:<12.4f} "
            f"{median_time:<12.4f} {max_time:<12.4f}"
        )

    print("Process pool results:")
    print("-" * 80)
    print(
        f"{'Workers':<10} {'Mean (s)':<12} {'Min (s)':<12} " f"{'Median (s)':<12} {'Max (s)':<12}"
    )
    print("-" * 80)

    for workers, timings in processes_results:
        mean_time = statistics.mean(timings)
        median_time = statistics.median(timings)
        min_time = min(timings)
        max_time = max(timings)
        print(
            f"{workers:<10} {mean_time:<12.4f} {min_time:<12.4f} "
            f"{median_time:<12.4f} {max_time:<12.4f}"
        )
