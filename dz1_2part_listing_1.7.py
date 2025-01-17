import time
import requests # Импортируем библиотеку requests для выполнения HTTP-запросов
import threading # Импортируем модуль threading для работы с потоками (многозадачности)

def read_example()->None: # Определяем функцию 'read_example', которая выполняет запрос и выводит статус
  response = requests.get('https://www.example.com')  # Отправляем GET-запрос на сайт example.com

  print(response.status_code)  # Выводим HTTP статус код ответа

sync_start = time.time() # Засекаем время начала выполнения синхронной версии

read_example()  # Вызываем функцию 'read_example' (первый запрос)
read_example()  # Вызываем функцию 'read_example' (второй запрос)

sync_end = time.time()# Засекаем время окончания выполнения синхронной версии

print(f'Время выполнение заняло {sync_end - sync_start:.4f} с.')

# Многопоточная версия

def read_example() -> None:
  response = requests.get('https://www.example.com')
  print(response.status_code)
  
thread_1 = threading.Thread(target=read_example)  # Создаем первый поток, который будет выполнять 'read_example'
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start() # Запускаем первый поток
thread_2.start()

print('Все потоки работают!') # Выводим сообщение, что оба потока запущены и работают

thread_1.join()# Ожидаем завершения первого потока
thread_2.join()
thread_end = time.time()

print(f'Время многопоточного выполнения заняло {thread_end - thread_start:.4f} с.')# Выводим время выполнения многопоточных запросов
