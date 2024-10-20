import time
from functools import wraps
from sklearn.ensemble import RandomForestClassifier
import pickle

X = [[3, 3, 3], [0, 3, 0], [3, 0, 0], [0, 0, 3]]
Y = ["q", "w", "w", "q"]

# Декоратор, который выводит время выполнения
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Затрачено {func.__name__} на выполнение {end - start:.8f} сек")
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
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

save_model(clf, "rf_model.pkl")  # Сохраняем модель с расширением .pkl
