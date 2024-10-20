import time
from functools import wraps
from sklearn.ensemble import RandomForestClassifier
from joblib import dump  #
X = [[3, 3, 3], [0, 3, 0], [3, 0, 0], [0, 0, 3]]
Y = ["q", "w", "w", "q"]

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
#Обучаем модель+измеряем время

@timethis
def train_model(X, Y):
    clf = RandomForestClassifier(n_estimators=10)
    return clf.fit(X, Y)
clf = train_model(X, Y)


@timethis
def save_model(model, filename):
    dump(model, filename)

save_model(clf, "rf_model.joblib")
