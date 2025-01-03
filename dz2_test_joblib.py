import time
from functools import wraps
from joblib import load
# Декоратор, который выводит время выполнения
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнена за {end - start:.8f} сек")
        return result
    return wrapper

@timethis
def load_m(filename):
    return load(filename)


rand_f_m = load_m("rf_model.joblib")

inp_data = [[0, 3, 0]]
prediction = rand_f_m.predict(inp_data)
print(f"Прогноз для {inp_data}: {prediction}")
