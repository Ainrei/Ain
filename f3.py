# импортируем time для создания задержек
import time
# импортируем multiprocessing для создания и управления дочерними процессами
import multiprocessing
# импортируем os, который предоставляет функции для взаимодействия с операционной системой
import os
# импортируем datetime для измерения времени выполнения
import datetime



# os.getpid() выводит идентификатор текущего исполняемого процесса Python
# time.sleep() приостанавливает выполнение на кол-во секунд
# datetime.datetime.now() определает текущее время

def hello_from_process01():
    print(f'Привет от дочернего процесса 01 {os.getpid()}!')
    time.sleep(3)
def hello_from_process02():
    print(f'Привет от дочернего процесса 02 {os.getpid()}!')
    time.sleep(5)
start=datetime.datetime.now()

# проверяем, запущен ли скрипт как основной модуль [if __name__ == '__main__']
# создаем новый процесс hello_processXX, который будет выполнять функцию hello_from_processXX [hello_process01 = multiprocessing.Process(target=hello_from_process01)]
# hello_process.start() запускает дочерний процесс
# hello_process.join() ожидает завершения дочернего процесса перед тем, как продолжить выполнение родительского процесса

if __name__ == '__main__':
    hello_process01 = multiprocessing.Process(target=hello_from_process01)
    hello_process01.start()
    hello_process02 = multiprocessing.Process(target=hello_from_process02)
    hello_process02.start()
    hello_process03 = multiprocessing.Process(target=hello_from_process02)
    hello_process03.start()
    hello_process04 = multiprocessing.Process(target=hello_from_process02)
    hello_process04.start()
    hello_process05 = multiprocessing.Process(target=hello_from_process02)
    hello_process05.start()
    hello_process06 = multiprocessing.Process(target=hello_from_process02)
    hello_process06.start()
    hello_process07 = multiprocessing.Process(target=hello_from_process02)
    hello_process07.start()
    hello_process08 = multiprocessing.Process(target=hello_from_process02)
    hello_process08.start()
    hello_process09 = multiprocessing.Process(target=hello_from_process02)
    hello_process09.start()
    hello_process010 = multiprocessing.Process(target=hello_from_process02)
    hello_process010.start()
    hello_process011 = multiprocessing.Process(target=hello_from_process02)
    hello_process011.start()
    print(f'Привет от родительского процесса {os.getpid()}')
    hello_process01.join()
    hello_process02.join()
    hello_process03.join()
    hello_process04.join()
    hello_process05.join()
    hello_process06.join()
    hello_process07.join()
    hello_process08.join()
    hello_process09.join()
    hello_process010.join()
    hello_process011.join()
finish= datetime.datetime.now()
print(finish-start)
