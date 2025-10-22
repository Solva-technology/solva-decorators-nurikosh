from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        arguments = (args, tuple(kwargs.items()))

        if arguments in cache:
            print("Из кэша")
            return cache[arguments]

        res = func(*args, **kwargs)

        cache[arguments] = res

        return res

    return wrapper
