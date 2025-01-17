# импортируем time для отслеживания времени выполнения
import time
# импортируем wraps из модуля functools, которая поможет сохранить оригинальные метаданные функции, когда она завернута декоратором
from functools import wraps


# декоратор, который выводит время выполнения
# внутри него определяется обертка wrapper, которая начинает отслеживание времени с помощью time.perf_counter(), затем вызывает оригинальную функцию с переданными аргументами и получает ее результат
# затем снова измеряется время с помощью time.perf_counter()

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} выполнен за {end - start:.8f} секунд")
        return result
    return wrapper


# применяем декоратор к функции Фибоначчи

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

# пример использования
number = 10
print(f"Число Фибоначчи {number} равно {fibonacci(number)}")
