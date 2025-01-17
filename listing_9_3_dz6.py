import asyncpg  # Импортируем библиотеку asyncpg для асинхронного взаимодействия 
from aiohttp import web  # Импортируем основной объект aiohttp для работы с веб-приложением
from aiohttp.web_app import Application  # Импортируем класс Application для создания веб-приложения
from aiohttp.web_request import Request  # Импортируем тип Request для работы с HTTP-запросами
from aiohttp.web_response import Response  # Импортируем тип Response для формирования HTTP-ответов
from asyncpg import Record  # Импортируем тип Record для работы с результатами запросов к базе данных
from asyncpg.pool import Pool  # Импортируем Pool для создания пула подключений к базе данных

routes = web.RouteTableDef()  # Создаем объект для хранения маршрутов веб-приложения (маршруты будут добавляться позже)

DB_KEY = 'database'  # Ключ для хранения и извлечения пула подключений к базе данных в приложении

# Обработчик для маршрута "/products/{id}", где {id} — это параметр в URL
@routes.get('/products/{id}')
async def get_product(request: Request) -> Response:
    try:
        str_id = request.match_info['id']  # Извлекаем параметр 'id' из URL (например, /products/1 -> id = 1)
        product_id = int(str_id)  # Преобразуем строковый параметр id в целое число

        query = """  # SQL-запрос для получения информации о товаре по его id.
        SELECT
            product_id,
            product_name,
            brand_id
        FROM product
        WHERE product_id = $1  # $1 — это параметр запроса, который будет заменен на product_id.
        """
        
        connection: Pool = request.app[DB_KEY]  # Получаем пул подключений из объекта приложения
        result: Record = await connection.fetchrow(query, product_id)  # Выполняем запрос и получаем одну запись о товаре
        
        if result is not None:  # Если результат запроса не пустой, возвращаем его как JSON-ответ
            return web.json_response(dict(result))  # Преобразуем запись в словарь и отправляем в ответ
        else:  # Если товар с таким id не найден, отправляем ошибку 404 (не найдено)
            raise web.HTTPNotFound()

    except ValueError:  # Если не удалось преобразовать id в число, отправляем ошибку 400 (неверный запрос)
        raise web.HTTPBadRequest()

# Функция для создания пула подключений к базе данных
async def create_database_pool(app: Application):
    print('Создается пул подключений.')  # Логируем создание пула
    
    # Создаем пул подключений к базе данных с указанными параметрами
    pool: Pool = await asyncpg.create_pool(
        host='127.0.0.1',  # Адрес сервера базы данных
        port=5432,  # Порт для подключения к базе данных PostgreSQL
        user='postgres',  # Имя пользователя базы данных
        password='password',  # Пароль
        database='products',  # Имя базы данных
        min_size=6,  # Минимальное количество подключений в пуле
        max_size=6,  # Максимальное
    )

    app[DB_KEY] = pool  # Сохраняем пул подключений в объект приложения, используя ключ DB_KEY

# Функция для закрытия пула подключений при завершении работы приложения
async def destroy_database_pool(app: Application):
    print('Уничтожается пул подключений.')  # Логируем уничтожение пула
    
    pool: Pool = app[DB_KEY]  # Извлекаем пул подключений из объекта приложения
    await pool.close()  # Закрываем пул подключений, освобождая все ресурсы

# Создаем объект веб-приложения
app = web.Application()

# Регистрируем функции для создания и уничтожения пула подключений при старте и завершении работы приложения
app.on_startup.append(create_database_pool)  # Запускается перед стартом приложения (создание пула)
app.on_cleanup.append(destroy_database_pool)  # Запускается при завершении работы приложения (закрытие пула)

# Добавляем маршруты, определенные в объекте routes, в приложение
app.add_routes(routes)

# Запускаем веб-сервер и начинаем слушать запросы
web.run_app(app
