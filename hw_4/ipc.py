import codecs
import multiprocessing as mp
import sys
import threading
import time
from datetime import datetime
from queue import Empty


def encode(text: str) -> str:
    return codecs.encode(text, "rot13")


def lower_case_worker(terminate, lower_case_queue, encode_queue):
    while not terminate.is_set():
        try:
            text = lower_case_queue.get(timeout=0.1)
            print(f"[{datetime.now()}] Lower case worker received {text}")
            encode_queue.put(text.lower())
            time.sleep(5)
        except Empty:
            continue


def encode_worker(terminate, encode_queue, main_queue):
    while not terminate.is_set():
        try:
            text = encode_queue.get(timeout=0.1)
            print(f"[{datetime.now()}] Encode worker received {text}")
            main_queue.put(encode(text))
        except Empty:
            continue


def reader_thread(terminate, lower_case_queue):
    for line in sys.stdin:
        line = line.strip()
        print(f"[{datetime.now()}] Main process read {line}")
        lower_case_queue.put(line)
    print("Terminate is set")
    terminate.set()


def output_result_thread(terminate, main_queue):
    while not terminate.is_set():
        try:
            result = main_queue.get(timeout=0.1)
            print(f"[{datetime.now()}] Main process received {result}")
        except Empty:
            continue


if __name__ == "__main__":
    terminate = mp.Event()
    lower_case_queue = mp.Queue()
    encode_queue = mp.Queue()
    main_queue = mp.Queue()

    lower_case_process = mp.Process(
        target=lower_case_worker, args=(terminate, lower_case_queue, encode_queue)
    )
    encode_process = mp.Process(target=encode_worker, args=(terminate, encode_queue, main_queue))
    lower_case_process.start()
    encode_process.start()

    reader = threading.Thread(target=reader_thread, args=(terminate, lower_case_queue))
    output_result = threading.Thread(target=output_result_thread, args=(terminate, main_queue))
    output_result.start()
    reader.start()
    output_result.join()
    reader.join()

    lower_case_process.join()
    encode_process.join()
