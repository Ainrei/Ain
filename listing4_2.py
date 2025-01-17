# импортируем asyncio для работы с асинхронным кодом в Python, который позволяет запускать несколько задач одновременно
import asyncio
# импортируем aiohttp для работы с HTTP-запросами
import aiohttp
# импортируем ClientSession для отправки HTTP-запросов в aiohttp
from aiohttp import ClientSession
# импортируем функцию-декоратор async_timed для измерения времени исполнения асинхронных функций
from util import async_timed


# прообраз DoS-атаки
# fetch_status - асинхронная функция, предназначенная для получения статуса HTTP-ответа указанного URL.
# Она принимает два параметра: session типа ClientSession и url типа str, а возвращает int

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    # используем контекстный менеджер для выполняется GET-запрос к указанному url
    async with session.get(url) as result:
        # после завершения запроса возвращается статус ответа (200 - успешно)
        return result.status

@async_timed()
async def main():
    # создаем асинхронную сессию ClientSession, которая использует контейнер async with. Это позволяет автоматически управлять жизненным циклом сессии (например, закрывать ее после использования).
    async with aiohttp.ClientSession() as session:
        # указываем URL, для которого будет выполнен запрос
        # затем вызываем функцию fetch_status, и сохраняем результат в переменной status и выводим сообщение о состоянии для указанного URL
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')
# запускаем асинхронную функцию main(), что инициирует выполнение всей программы
asyncio.run(main())
