from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arguments = [repr(a) for a in args]
        k_arguments = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        all_args = ", ".join(arguments + k_arguments)

        print(f"Вызов: {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")

        return result

    return wrapper
