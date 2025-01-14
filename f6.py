import time
from functools import wraps

# Декоратор, который выводит время выполнения.
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} выполнен за {end - start:.8f} секунд")
        return result
    return wrapper

@timethis
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Пример использования
number = 10
print(f"Число Фибоначчи {number} равно {fibonacci(number)}")
