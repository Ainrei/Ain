import asyncio
#from util import delay вместо этого функция delay:
async def delay (delay_second: int) -> int:
#какой тип переменной возвращает функция, лучше всегда указывать
    print (f'засыпаю на {delay_second} секунд')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} cек закончился')
    return delay_second

async def main():
    sleep_for_three = asyncio.create_task(delay(10))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(8))
    await sleep_for_three
    await sleep_again
    await sleep_once_more
asyncio.run(main())
