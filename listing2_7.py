#2.7 листинг
import asyncio

async def delay (delay_second: int) -> int:
#какой тип переменной возвращает функция, лучше всегда указывать
    print (f'засыпаю на {delay_second} секунд')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} cек закончился')
    return delay_second

async def add_one(number: int) -> int:
    return number + 1 
    #питон отдает все мощности на calculate
async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'
async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one) #выведет число int
    print(message)
asyncio.run(main())
