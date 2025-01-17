def frange(start, stop, increment):
x = start
while x < stop:
yield x
x += increment

for n in frange(0, 4, 0.5):
print(n)

list(frange(0, 1, 0.125))

def countdown(n):
print('Starting to count from', n)
while n > 0:
yield n
n -= 1
print('Done!')



# Создает генератор – обратите внимание на отсутствие вывода
c = countdown(3)
c

# Выполняется до первого yield и выдает значение
next(c)

# Выполняется до следующего yield
next(c)

# Выполняется до следующего yield
next(c)

# Выполняется до следующего yield (итерирование останавливается)
next(c)
