from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (float, int)) or arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")
        for _, arg in kwargs:
            if not isinstance(arg, (float, int)) or arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper
