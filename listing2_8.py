# импортируем asyncio для работы с асинхронным кодом в Python, который позволяет запускать несколько задач одновременно
import asyncio

# определяется асинхронная функция delay, которая принимает аргумент delay_second типа int 
async def delay (delay_second: int) -> int:
    # выводит сообщение о том, на сколько секунд идет задержка.
    print (f'засыпаю на {delay_second} секунд')
    # "засыпает" на указанное количество секунд (используется await, чтобы не блокировать выполнение других задач)
    await asyncio.sleep(delay_second)
    # после завершения времени ожидания выводится сообщение о завершении задержки
    print(f'сон в течение {delay_second} cек закончился')
    # возвращает значение delay_second, то есть количество секунд, на которые она "заснула"
    return delay_second

# определяется асинхронная функция main, которая будет основной точкой входа

async def main():
    # вызывается функция delay с аргументом 3, и результат сохраняется в переменной sleep_for_three
    # функция asyncio.create_task создает задачу, которой нужно на выполнение 3с
    sleep_for_three = asyncio.create_task(delay(3))
    # печатаем тип задачи
    print(type(sleep_for_three))
    # ожидаем завершения задачи sleep_for_three, и результат (количество секунд) сохраняем в переменной result.
    result = await sleep_for_three
    print(result)
asyncio.run(main())
