import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)

# Загружаем датасет пингвинов
df_penguins = sns.load_dataset('penguins')

# species: Вид пингвина (Adelie, Chinstrap, Gentoo).
# island: Остров, на котором был найден пингвин (Torgersen, Dream, или Biscoe).
# bill_length_mm: Длина клюва в миллиметрах.
# bill_depth_mm: Глубина клюва в миллиметрах.
# flipper_length_mm: Длина ласт в миллиметрах.
# body_mass_g: Масса тела в граммах.
# sex: Пол пингвина.

df_penguins = df_penguins.dropna()

# Преобразуем категорию 'species' в числовой формат
df_penguins['species'] = df_penguins['species'].astype('category').cat.codes

# Оставляем только числовые столбцы для агрегации
numeric_columns = df_penguins.select_dtypes(include=[np.number])

# Добавляем обратно категорию species для группировки
numeric_columns['species'] = df_penguins['species']

# Рассчитаем среднее и стандартное отклонение для каждого вида (только для числовых столбцов)
distribution_params = numeric_columns.groupby('species').agg(['mean', 'std']).reset_index()

# Список имен столбцов
distribution_params.columns = ['species'] + [f'{col}_{stat}' for col, stat in distribution_params.columns[1:]]

# Количество новых записей для генерации
num_samples = 10000 

def generate_samples(means, stds, num_samples):
    return np.random.normal(loc=means, scale=stds, size=(num_samples, len(means)))

# Генерация данных
samples = []
species_list = []
for _, params in distribution_params.iterrows():
    means = params.filter(like='mean').values
    stds = params.filter(like='std').values
    generated_samples = generate_samples(means, stds, num_samples)
    samples.append(generated_samples)
    species_list.append(np.full(num_samples, params['species']))

# Объединяем сгенерированные данные в один DataFrame
generated_columns = [col for col in distribution_params.columns if '_mean' in col]
df_generated = pd.DataFrame(np.vstack(samples), columns=generated_columns)

# Добавляем столбец с метками видов
df_generated['species'] = np.concatenate(species_list)

df_generated.columns = [col.replace('_mean', '') for col in df_generated.columns]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', palette='deep')
plt.title('Характеристики пингвинов в зависимости от их вида')
plt.xlabel('Длина клюва (мм)')
plt.ylabel('Глубина клюва (мм)')
plt.legend(title='Вид', labels=['Adelie', 'Chinstrap', 'Gentoo'])
plt.show()

X = df_generated.drop('species', axis=1)
y = df_generated['species']

# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Байесовский классификатор
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# Предсказания на тестовой выборке
nb_predictions = nb_classifier.predict(X_test)

accuracy = accuracy_score(y_test, nb_predictions)
print(f"Точность Байесовского классификатора: {accuracy:.4f}")

# Матрица ошибок (confusion matrix)
conf_matrix = confusion_matrix(y_test, nb_predictions)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Adelie', 'Chinstrap', 'Gentoo'],
            yticklabels=['Adelie', 'Chinstrap', 'Gentoo'])
plt.title('Матрица ошибок (Confusion Matrix)')
plt.xlabel('Предсказано')
plt.ylabel('Фактическое')
plt.show()
