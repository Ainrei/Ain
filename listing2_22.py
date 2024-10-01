# async нид, потому что task относится к библиотеке async// какой тип переменной возвращает функция - указывать
import asyncio
async def delay(delay_second: int)-> int:
    print(f'засыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'сон в течение{delay_second} c закончился')
    return delay_second

def call_later():
    print("Меня вызовут в ближайшем будущем!")
async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main(),debug=True)
