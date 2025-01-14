import time
from functools import wraps

# Декоратор, который выводит время выполнения.
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнен за {end - start:.8f} секунд")
        return result
    return wrapper

@timethis
def factorial(n=3):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Пример использования
number = 5
print(f"Факториал {number} равен {factorial(number)}")
