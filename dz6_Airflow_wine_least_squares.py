from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
from graphviz import Digraph
import os

# Функция для загрузки данных
def load_data():
    print("Загрузка данных.")
    wine = load_wine()
    data = wine.data
    target = wine.target
    print(f"Данные успешно загружены. Размер данных: {data.shape}")
    return data, target

# Функция для нормализации данных
def normalize_data(data):
    print("Нормализация данных.")
    data_normalized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    print("Нормализация завершена.")
    return data_normalized

# Функция для разделения данных на обучающую и тестовую выборки
def split_data(data, target):
    print("Разделение данных на обучающую и тестовую выборки.")
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=1)
    print("Разделение завершено.")
    return X_train, X_test, y_train, y_test

# Функция для применения метода наименьших квадратов (МНК)
def apply_least_squares(X_train, y_train):
    print("Применение метода наименьших квадратов.")
    X = np.c_[np.ones(X_train.shape[0]), X_train]
    theta = np.linalg.inv(X.T @ X) @ X.T @ y_train
    print("МНК завершен. Параметры: ", theta)
    return theta

# Функция для анализа результатов
def analyze_results(X_test, y_test, theta):
    print("Анализ результатов.")
    X = np.c_[np.ones(X_test.shape[0]), X_test]
    y_pred = X @ theta
    print("Анализ завершен.")
    return y_pred

# Функция для визуализации результатов
def plot_results(y_test, y_pred):
    print("Построение графика.")
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(y_test)), y_test, color='blue', label='Фактические значения')
    plt.scatter(range(len(y_pred)), y_pred, color='red', label='Прогнозируемые значения')
    plt.title('Фактические и прогнозируемые значения')
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid()
    plt.show()

# Функция для оценки модели
def evaluate_model(y_test, y_pred):
    print("Оценка модели.")
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Оценка завершена. R^2: {r2}, MAE: {mae}")

# Функция для создания и сохранения графа DAG с помощью Graphviz
def draw_dag_graph():
    dot = Digraph(comment='DAG: Метод наименьших квадратов с датасетом Wine', format='png')
    dot.attr(fontname='Arial', fontsize='12')

    # Определяем узлы (шаги DAG)
    dot.node('A', 'Загрузка данных', style='filled', fillcolor='#FFCC80', shape='box', fontsize='10')
    dot.node('B', 'Нормализация данных', style='filled', fillcolor='#90CAF9', shape='box', fontsize='10')
    dot.node('C', 'Разделение данных', style='filled', fillcolor='#A5D6A7', shape='box', fontsize='10')
    dot.node('D', 'Применение МНК', style='filled', fillcolor='#FFAB91', shape='box', fontsize='10')
    dot.node('E', 'Анализ результатов', style='filled', fillcolor='#FFCC80', shape='box', fontsize='10')
    dot.node('F', 'Визуализация результатов', style='filled', fillcolor='#80CBC4', shape='box', fontsize='10')
    dot.node('G', 'Оценка модели', style='filled', fillcolor='#FFAB91', shape='box', fontsize='10')

    # Определяем зависимости между узлами
    dot.edge('A', 'B', label='1')  # Загрузка -> Нормализация
    dot.edge('B', 'C', label='2')  # Нормализация -> Разделение
    dot.edge('C', 'D', label='3')  # Разделение -> Применение МНК
    dot.edge('D', 'E', label='4')  # Применение МНК -> Анализ
    dot.edge('E', 'F', label='5')  # Анализ -> Визуализация
    dot.edge('D', 'G', label='6')  # Применение МНК -> Оценка

    # Сохраняем граф как изображение
    output_path = '/content/dag_wine_least_squares_workflow'
    dot.render(output_path, cleanup=True)
    print(f"Граф DAG сохранен как '{output_path}.png'")

# Вызов функции для рисования графа
draw_dag_graph()

# Проверка наличия файла
file_path = '/content/dag_wine_least_squares_workflow.png'
if os.path.exists(file_path):
    print("Файл найден:", file_path)
else:
    print("Файл не найден.")

# Отображение графа
from IPython.display import Image
Image(file_path)

# Вызов всех функций для выполнения
data, target = load_data()
data_normalized = normalize_data(data)
X_train, X_test, y_train, y_test = split_data(data_normalized, target)
theta = apply_least_squares(X_train, y_train)
y_pred = analyze_results(X_test, y_test, theta)
plot_results(y_test, y_pred)
evaluate_model(y_test, y_pred)
