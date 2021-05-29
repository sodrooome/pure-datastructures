import time


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
