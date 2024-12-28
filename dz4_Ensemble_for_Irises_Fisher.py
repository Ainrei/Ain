import asyncio
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import nest_asyncio

# Для разрешения вложенного выполнения асинхронных функций
nest_asyncio.apply()

# Ирисы Фишера
iris = load_iris()
df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
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

# Количество новых записей для генерации
num_samples = 10**6

def generate_samples(params, num_samples):
    means = params.filter(like='mean').values
    stds = params.filter(like='std').values
    return np.random.normal(loc=means, scale=stds, size=(num_samples, len(means)))

async def async_generate_samples(params, num_samples):
# асинхронная функция для вызова generate_samples в отдельном фоновом потоке, не блокируя основной поток выполнения
    return await asyncio.to_thread(generate_samples, params, num_samples)

async def main():
    tasks = [] # Для хранения асинхронных задач
    for species, params in distribution_params.iterrows(): # По каждой строке
        tasks.append(async_generate_samples(params, num_samples))

    # Ждем завершения всех задач
    results = await asyncio.gather(*tasks)

    # Генерируем данные для каждого вида ириса и объединяем в один DataFrame
    df_generated = pd.concat(
        [pd.DataFrame(result, columns=iris['feature_names']).assign(species=species) for result, species in zip(results, distribution_params.index)],
        ignore_index=True
    )

    print(f"Размер сгенерированного датафрейма: {df_generated.shape}")

    # Преобразуем категорию species в числовой формат
    df_generated['species'] = df_generated['species'].astype('category').cat.codes

    # Разделяем данные на признаки и целевую переменную
    X = df_generated.drop('species', axis=1)
    y = df_generated['species']

    # Разделяем на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Ансамблевый классификатор
    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(X_train, y_train)
    log_reg_predictions = log_reg.predict_proba(X_train)

    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=1)
    rf_classifier.fit(log_reg_predictions, y_train)

    log_reg_test_predictions = log_reg.predict_proba(X_test)
    rf_predictions = rf_classifier.predict(log_reg_test_predictions)

    # Оценка точности ансамбля
    accuracy = accuracy_score(y_test, rf_predictions)
    print(f"Точность ансамбля (логистическая регрессия + Random Forest): {accuracy:.4f}")

    # Матрица ошибок (confusion matrix)
    conf_matrix = confusion_matrix(y_test, rf_predictions)

    # Визуализация матрицы ошибок
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Setosa', 'Versicolor', 'Virginica'],
                yticklabels=['Setosa', 'Versicolor', 'Virginica'])
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
