import asyncio

async def delay (delay_second: int) -> int:
#какой тип переменной возвращает функция, лучше всегда указывать
    print (f'засыпаю на {delay_second} секунд')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} cек закончился')
    return delay_second

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)
asyncio.run(main())
