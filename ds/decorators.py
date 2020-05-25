import time

"""
class Benchmark:
    # Class decorators for benchmarking code.

    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        execute_time = end_time - start_time
        value = self.function(*args, **kwargs)
        msg = "Runtime for took {time:.3f} seconds."
        print(msg.format(time=execute_time))
        return value
"""

def benchmark(func):
    """Benchmark decorators using time module."""

    def run_benchmark(*args, **kwargs):
        start = time.time()
        end = time.time()
        runtime = end - start
        value = func(*args, **kwargs)
        msg = "Runtime for {func} took {time:.3f} seconds."
        print(msg.format(func=func.__name__, time=runtime))
        return value
    return run_benchmark