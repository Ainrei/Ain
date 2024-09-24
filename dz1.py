import time
from functools import wraps
def timethis(func):
# Декоратор, который выводит время выполнения.
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def f(x, y, z):
             return x + y + z
result = f(1, 2, 3)
print(result)

# Пример
