import asyncio
#from util import delay вместо этого функция delay:
async def delay (delay_second: int) -> int:
#async нужен, потому что task относится к библиотеке async
#какой тип переменной возвращает функция, лучше всегда указывать
    print (f'засыпаю на {delay_second} секунд')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} cек закончился')
    return delay_second

#первый вариант функции
async def main():
    tasks = []
    for _ in range(10):  # Создаем 10 задач, можно 1000, но выводить много будет
        task = asyncio.create_task(delay(3))
        tasks.append(task)

    # Ждем завершения всех задач
    await asyncio.gather(*tasks)
asyncio.run(main())


#второй вариант функции
async def main():
    xs = [asyncio.create_task(delay(x)) for x in range(10)]
    for x in xs:
        await x
asyncio.run(main())
