def frange(start, stop, increment):  # Определяем функцию генератора, которая принимает три параметра: начало, конец и шаг
x = start  # Инициализируем переменную x значением start
while x < stop: # Пока x меньше stop, продолжаем генерировать значения
yield x #yield превращает функцию в генератор +# Возвращаем текущее значение x и приостанавливаем выполнение функции
x += increment # Увеличиваем x на заданный шаг increment

for n in frange(0, 4, 0.5): # Цикл, который будет перебирать значения, генерируемые генератором frange от 0 до 4 с шагом 0.5
print(n)

list(frange(0, 1, 0.125)) # Преобразуем генератор в список, чтобы получить все значения в диапазоне от 0 до 1 с шагом 0.125

def countdown(n): # Функция countdown принимает число n и генерирует отсчет
print('Starting to count from', n) # Выводим сообщение о начале отсчета
while n > 0: # Пока n больше 0, продолжаем отсчет
yield n # Генерируем текущее значение n и приостанавливаем выполнение функции
n -= 1 # Уменьшаем n на 1
print('Done!') # После завершения отсчета выводим сообщение "Done!"

# Создаем генератор countdown с начальным значением 3- обратите внимание на отсутствие вывода
c = countdown(3)
c # Печатает объект генератора, но сам генератор еще не запущен
# Выполняется до первого yield и выдает значение
next(c) # Выводит 3, выполнение генератора приостанавливается на первой метке yield
# Выполняется до следующего yield
next(c)
# Выполняется до следующего yield
next(c)
# Выполняется до следующего yield (итерирование останавливается)
next(c)
