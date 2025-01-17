import time
from functools import wraps
def timethis(func):
# Декоратор, который выводит время выполнения
    @wraps(func) # Используем wraps для сохранения метаданных функции 'func'
    def wrapper(*args, **kwargs): # Определяем внутреннюю функцию 'wrapper', которая обертывает вызов оригинальной функции
        start = time.time()
        result = func(*args, **kwargs) # Вызываем оригинальную функцию с аргументами *args и **kwargs и сохраняем результат.
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def f(x, y, z):
             return x + y + z
result = f(1, 2, 3)
print(result)


