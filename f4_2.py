# импортируем time для отслеживания времени выполнения
import time
# импортируем threading для создания и управления потоками
import threading
# импортируем requests для выполнения HTTP-запросов
import requests


# получаем данные с веб-страницы по адресу [requests.get('https://www.example.com')]
# response.status_code выводит код состояния (200 - успешный, 404 - неуспешный)

def read_example() -> None:
  response = requests.get('https://www.example.com')
  print(response.status_code)

#  создаем два потока, которые будут выполнять функцию read_example
thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

# записываем начальное время
thread_start = time.time()

# запускаем потоки
thread_1.start()
thread_2.start()
print('Все потоки работают!')

# ожидаем завершения потоков
thread_1.join()
thread_2.join()

# записываем конечное время
thread_end = time.time()

# пишем, сколько времени заняло
print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')
