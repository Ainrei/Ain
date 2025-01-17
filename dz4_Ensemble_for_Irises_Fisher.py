# Импортируем модуль asyncio для работы с асинхронным программированием
import asyncio
# Импортируем библиотеку numpy для работы с многомерными массивами и матрицами
import numpy as np
# Импортируем pandas для работы с данными в табличной форме (DataFrame)
import pandas as pd
# Импортируем функцию load_iris из модуля sklearn.datasets для загрузки набора данных "Ирисы Фишера"
from sklearn.datasets import load_iris
# Импортируем функцию train_test_split из sklearn.model_selection для разбиения данных на обучающие и тестовые наборы
from sklearn.model_selection import train_test_split
# Импортируем модель логистической регрессии из sklearn.linear_model
from sklearn.linear_model import LogisticRegression
# Импортируем классификатор случайного леса из sklearn.ensemble
from sklearn.ensemble import RandomForestClassifier
# Импортируем метрики для оценки качества модели: accuracy_score и confusion_matrix
from sklearn.metrics import accuracy_score, confusion_matrix

# Импортируем seaborn для создания красивых визуализаций.
import seaborn as sns
import matplotlib.pyplot as plt
# Импортируем nest_asyncio для поддержки асинхронного программирования в уже существующих циклах событий (например, в Jupyter)
import nest_asyncio


# Для разрешения вложенного выполнения асинхронных функций
nest_asyncio.apply()

# Ирисы Фишера
# Загружаем набор данных "Ирисы Фишера" с помощью функции load_iris из sklearn.datasets
iris = load_iris()

# Преобразуем данные о признаках (features) в DataFrame с помощью pandas
# Столбцы данных будут соответствовать именам признаков (feature_names)
df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

# Добавляем столбец 'species' в DataFrame, который будет содержать метки классов.
# Используем pd.Categorical.from_codes для создания категориального столбца на основе кодов в iris['target']
# и соответствующих названий классов из iris['target_names']
df['species'] = pd.Categorical.from_codes(iris['target'], iris['target_names'])

# Рассчитаем среднее и стандартное отклонение для каждого вида
distribution_params = df.groupby('species').agg(['mean', 'std'])

# sepal length (cm) — длина чашелистика,
# sepal width (cm) — ширина чашелистика,
# petal length (cm) — длина лепестка,
# petal width (cm) — ширина лепестка.

# Переименуем столбцы
distribution_params.columns = [
    'sepal_length_mean', 'sepal_length_std',
    'sepal_width_mean', 'sepal_width_std',
    'petal_length_mean', 'petal_length_std',
    'petal_width_mean', 'petal_width_std'
]

# Количество новых записей для генерации 1 млн
num_samples = 10**6

def generate_samples(params, num_samples):
    # Извлекаем значения среднего для каждого признака, фильтруя столбцы, содержащие 'mean'
    means = params.filter(like='mean').values
    
    # Извлекаем значения стандартного отклонения для каждого признака, фильтруя столбцы, содержащие 'std'
    stds = params.filter(like='std').values
    
    # Генерируем выборки с помощью нормального распределения
    # np.random.normal генерирует выборки с указанным средним (means) и стандартным отклонением (stds)
    # Размер выборки — num_samples, количество признаков — len(means)
    return np.random.normal(loc=means, scale=stds, size=(num_samples, len(means)))

async def async_generate_samples(params, num_samples): # асинхронная функция для вызова generate_samples в отдельном фоновом потоке, не блокируя основной поток выполнения

    return await asyncio.to_thread(generate_samples, params, num_samples) # Выполняем generate_samples в фоновом потоке с использованием asyncio.to_thread

async def main():
    tasks = [] # Для хранения асинхронных задач
    for species, params in distribution_params.iterrows():  # Итерируем по каждой строке в distribution_params (данные о распределении признаков для каждого вида ириса)
        tasks.append(async_generate_samples(params, num_samples)) # Добавляем асинхронную задачу для генерации выборок

    # Ждем завершения всех задач
    results = await asyncio.gather(*tasks)
# После завершения задач генерируем DataFrame для каждого вида ириса и объединяем все результаты в один DataFrame
    
    df_generated = pd.concat(
        [pd.DataFrame(result, columns=iris['feature_names']).assign(species=species) # Создаем DataFrame для каждой генерации и добавляем столбец вида
         for result, species in zip(results, distribution_params.index)], # Сопоставляем результаты и индексы (вида ириса)
        ignore_index=True # Игнорируем индексы для корректного объединения
    )

    print(f"Размер сгенерированного датафрейма: {df_generated.shape}")

    # Преобразуем категорию species в числовой формат
    df_generated['species'] = df_generated['species'].astype('category').cat.codes

    # Разделяем данные на признаки и целевую переменную
    X = df_generated.drop('species', axis=1)
    y = df_generated['species']

    # Разделяем на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Ансамблевый классификатор (cоздаем+обучеаем логистическую регрессию)
    log_reg = LogisticRegression(max_iter=1000) #max число итераций задаем
    log_reg.fit(X_train, y_train) # Обучаем модель на обучающих данных
    log_reg_predictions = log_reg.predict_proba(X_train) # Получаем вероятности предсказаний на обучающих данных
    
    # Создаем и обучаем классификатор случайного леса
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=1) # 100 деревьев в лесу
    rf_classifier.fit(log_reg_predictions, y_train) # Обучаем модель случайного леса на предсказаниях логистической регрессии

    log_reg_test_predictions = log_reg.predict_proba(X_test) # Получаем предсказания для тестовых данных с помощью логистической регрессии
    rf_predictions = rf_classifier.predict(log_reg_test_predictions) # Получаем предсказания с помощью случайного леса на основе предсказаний логистической регрессии

    # Оценка точности ансамбля
    accuracy = accuracy_score(y_test, rf_predictions)
    print(f"Точность ансамбля (логистическая регрессия + Random Forest): {accuracy:.4f}")

    # Матрица ошибок (confusion matrix)
    conf_matrix = confusion_matrix(y_test, rf_predictions)

    # Визуализация матрицы ошибок
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Setosa', 'Versicolor', 'Virginica'],
                yticklabels=['Setosa', 'Versicolor', 'Virginica'])  # Аннотируем матрицу с подписями классов
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

# Создаем асинхронную функцию для запуска main
async def run():
    await main()
# Дождаться завершения всех асинхронных задач в main, прежде чем продолжить выполнение следующего кода 

# Запускаем асинхронную функцию
asyncio.run(run())
