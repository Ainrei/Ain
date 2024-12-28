from graphviz import Digraph

def draw_flowchart():
    # Создаем объект Digraph для построения схемы
    dot = Digraph(comment='Алгоритм классификации пингвинов')
    dot.attr(fontname='Arial', fontsize='12')

    dot.node('A', 'Загрузка данных', style='filled', fillcolor='#FFCC80', shape='box', fontsize='10')
    dot.node('B', 'Очистка данных', style='filled', fillcolor='#FFAB91', shape='box', fontsize='10')
    dot.node('C', 'Преобразование категориальной\nпеременной виды пингвинов \nв числа', style='filled', fillcolor='#80CBC4', shape='box', fontsize='10')
    dot.node('D', 'Расчёт среднего и\nстандартного отклонения\nдля генерации', style='filled', fillcolor='#90CAF9', shape='box', fontsize='10')
    dot.node('E', 'Генерация новых данных', style='filled', fillcolor='#A5D6A7', shape='box', fontsize='10')
    dot.node('F', 'Диаграмма рассеяния', style='filled', fillcolor='#CE93D8', shape='box', fontsize='10')
    dot.node('G', 'Разделение на\nобучение/тест', style='filled', fillcolor='#FFCDD2', shape='box', fontsize='10')
    dot.node('H', 'Обучение -\nНаивный байесовский\nклассификатор', style='filled', fillcolor='#FFD54F', shape='box', fontsize='10')
    dot.node('I', 'Прогноз на тестовой выборке', style='filled', fillcolor='#64B5F6', shape='box', fontsize='10')
    dot.node('J', 'Оценка точности модели', style='filled', fillcolor='#4DB6AC', shape='box', fontsize='10')
    dot.node('K', 'Матрица ошибок', style='filled', fillcolor='#F06292', shape='box', fontsize='10')

    # Добавляем стрелки между шагами
    dot.edge('A', 'B', label='Шаг 1')  # Загрузка данных -> Очистка данных
    dot.edge('B', 'C', label='Шаг 2')  # Очистка данных -> Преобразование species
    dot.edge('C', 'D', label='Шаг 3')  # Преобразование species -> Расчёт среднего и ст. отклонения
    dot.edge('D', 'E', label='Шаг 4')  # Расчёт среднего -> Генерация новых данных
    dot.edge('E', 'F', label='Шаг 5')  # Генерация новых данных -> Диаграмма рассеяния
    dot.edge('E', 'G', label='Шаг 6')  # Генерация новых данных -> Разделение на обучение/тест
    dot.edge('G', 'H', label='Шаг 7')  # Разделение на выборки -> Наивный байесовский классификатор
    dot.edge('H', 'I', label='Шаг 8')  # Наивный байесовский классификатор -> Прогноз
    dot.edge('I', 'J', label='Шаг 9')  # Прогноз -> Оценка модели
    dot.edge('I', 'K', label='Шаг 10') # Прогноз -> Матрица ошибок

    dot.render('схема_классификации_пингвинов', format='png', cleanup=True)

draw_flowchart()
