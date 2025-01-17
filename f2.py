import threading # Импортируем модуль threading для работы с потоками
def hello_from_thread():  # Определяем функцию, которая будет выполняться в отдельном потоке
    print(f'Привет от потока {threading.current_thread()}!') # Выводим информацию о текущем потоке, используя threading.current_thread()
    print(2+2) # выводим результат операции 2+2, для демонстрации работы функции
hello_thread = threading.Thread(target=hello_from_thread) # Создаем объект потока, указывая, что в нем будет выполняться функция hello_from_thread
hello_thread.start() # Запускаем поток, начинает выполнение функции hello_from_thread
total_threads = threading.active_count() # Получаем количество активных потоков в данный момент (включая основной поток)
thread_name = threading.current_thread().name  # Получаем имя текущего потока (имя основного потока)
print(f'В данный момент Python выполняет {total_threads} поток(ов)')  # Выводим количество активных потоков
print(f'Имя текущего потока {thread_name}') # Выводим имя текущего потока
#hello_thread.join()\ ---блокирует выполнение основного потока до завершения потока hello_thread
