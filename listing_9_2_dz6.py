# импортируем asyncpg для асинхронного взаимодействия с PostgreSQL
import asyncpg
# импортируем aiohttp, чтобы создавать веб-серверы и обрабатывать HTTP-запросы в асинхронном режиме
from aiohttp import web
# импортируем web для управления веб приложением
from aiohttp.web_app import Application
# импортируем Request для извлечени информации из запросов
from aiohttp.web_request import Request
# импортируем Response для формирования ответов от веб-приложения
from aiohttp.web_response import Response
# импортируем Record для обработки результатов из базы данных
from asyncpg import Record
# импортируем Pool для управления несколькими подключениями
from asyncpg.pool import Pool
# импортируем List, Dict аннотации типов 
from typing import List, Dict


# создаем объект маршрутов и ключ для хранения пула подключений к базе данных
routes = web.RouteTableDef()
DB_KEY = 'database'


#  асинхронная функция создает пул подключений к базе данных PostgreSQL и сохраняет его в объекте приложения

async def create_database_pool(app: Application):
 print('Создается пул подключений.')
 pool: Pool = await asyncpg.create_pool(host='127.0.0.1',
 port=5432,
 user='postgres',
 password='password',
 database='products',
 min_size=6,
 max_size=6)
 app[DB_KEY] = pool


# функция вызывается при завершении работы приложения и закрывает пул подключений

async def destroy_database_pool(app: Application):
 print('Уничтожается пул подключений.')
 pool: Pool = app[DB_KEY]
 await pool.close()


# определяется маршрут /brands, который обрабатывает GET-запросы.
# он выполняет SQL-запрос для получения всех брендов и возвращает их в виде JSON-ответа.

@routes.get('/brands')
async def brands(request: Request) -> Response:
connection: Pool = request.app[DB_KEY]
 brand_query = 'SELECT brand_id, brand_name FROM brand'
 results: List[Record] = await connection.fetch(brand_query)
 result_as_dict: List[Dict] = [dict(brand) for brand in results]
 return web.json_response(result_as_dict)


# Настройка и запуск приложения
# создается экземпляр приложения web.Application.
# функции по созданию и уничтожению пула подключений добавляются в обработчики событий запуска и завершения приложения.
# маршруты добавляются в приложение и запускается веб-сервер


app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)
app.add_routes(routes)
web.run_app(app)
