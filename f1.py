# импортируем os, который предоставляет функции для взаимодействия с операционной системой
import os
# импортируем threading, который позволяет создавать и управлять потоками
import threading

#  os.getpid() выводит идентификатор текущего исполняемого процесса Python
print(f'Исполняется Python-процесс с идентификатором: {os.getpid()}')

# получаем счетчик активных потоков и имя текущего потока
total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент Python исполняет {total_threads} поток(ов)')
print(f'Имя текущего потока {thread_name}')
