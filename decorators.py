import time


def timed(func):
    def decorator(self, *args, **kwargs):
        start = time.perf_counter()
        result = func(self, *args, **kwargs)
        end = time.perf_counter()
        if hasattr(self, "logger"):
            self.logger.info("%s took %ss", func.__name__, round(end - start, 2))
        return result

    return decorator
