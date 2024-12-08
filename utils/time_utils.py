import time


def execute(funs,  *args):
    for i, fun in enumerate(funs):
        print(f"\n========")
        start = time.time()
        fun(*args)
        end = time.time()
        elapsed_time_ms = (end - start) * 1000
        print(f"Elapsed time: {elapsed_time_ms}ms")
