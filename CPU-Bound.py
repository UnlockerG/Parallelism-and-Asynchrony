import platform
import random
import sys
import time
import psutil
from hashlib import md5
from multiprocessing import Manager, Process


def get_core_id():
    return None


def bruteforcer(queue, worker_id, core_id=None):
    if (core_id == get_core_id()) is not None:
        print(f"Worker {worker_id} is running on {core_id} core")

    while True:
        source_string = "".join(random.choices("0123456789", k=50))
        encoded_hash = md5(source_string.encode('utf8')).hexdigest()

        if encoded_hash.endswith("00000"):
            queue.put(f"{source_string} {encoded_hash}")


def main():
    hashes_target = 32
    workers_amount = 100
    hashes_queue = Manager().Queue()

    for worker_id in range(workers_amount):
        Process(target=bruteforcer, args=(hashes_queue, worker_id), daemon=True).start()

    start_time = time.time()
    hashes_found = 0
    while True:
        print(hashes_queue.get())
        hashes_found += 1

        if hashes_found == hashes_target:
            print(f"{workers_amount} workers found {hashes_target} hashes in {round(time.time() - start_time, 2)} sec.")
            sys.exit()


if __name__ == "__main__":
    main()