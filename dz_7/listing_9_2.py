import os
import asyncpg
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool
from typing import List, Dict

# Определяем маршруты для нашего веб-приложения
routes = web.RouteTableDef()

# Ключ для хранения пула подключений в объекте приложения
DB_KEY = 'database'

# Функция для создания пула подключений к базе данных
async def create_database_pool(app: Application):
    print('Создается пул подключений.')
    # Создаем пул подключений к базе данных PostgreSQL
    pool: Pool = await asyncpg.create_pool(
        host=os.getenv('DB_HOST', '127.0.0.1'),  # Получаем адрес хоста из переменных окружения, если не указано — 127.0.0.1
        port=int(os.getenv('DB_PORT', 5432)),  # Получаем порт базы данных (по умолчанию 5432)
        user=os.getenv('DB_USER', 'postgres'),  # Получаем имя пользователя для подключения
        password=os.getenv('DB_PASSWORD', 'password'),  # Получаем пароль
        database=os.getenv('DB_NAME', 'products'),  # Получаем имя базы данных
        min_size=6,  # Минимальное количество соединений в пуле
        max_size=6   # Максимальное количество соединений в пуле
    )
    # Сохраняем пул подключений в объекте приложения, чтобы к нему можно было обратиться позже
    app[DB_KEY] = pool

# Функция для уничтожения пула подключений при завершении работы приложения
async def destroy_database_pool(app: Application):
    print('Уничтожается пул подключений.')
    # Получаем пул подключений из приложения
    pool: Pool = app[DB_KEY]
    # Закрываем все соединения в пуле
    await pool.close()

# Обработчик маршрута '/brands' для получения списка брендов
@routes.get('/brands')
async def brands(request: Request) -> Response:
    # Получаем пул подключений из приложения
    connection: Pool = request.app[DB_KEY]
    # SQL-запрос для получения всех брендов
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    # Выполняем запрос и получаем результаты как список записей
    results: List[Record] = await connection.fetch(brand_query)
    # Преобразуем результаты в список словарей для удобства
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    # Возвращаем данные в формате JSON
    return web.json_response(result_as_dict)

# Создаем приложение aiohttp
app = web.Application()
# Добавляем функцию для создания пула подключений на этапе запуска
app.on_startup.append(create_database_pool)
# Добавляем функцию для уничтожения пула подключений на этапе завершения
app.on_cleanup.append(destroy_database_pool)
# Регистрируем маршруты в приложении
app.add_routes(routes)

# Запускаем веб-сервер
web.run_app(app)
