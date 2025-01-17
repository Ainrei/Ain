from aiohttp import web  # Импортируем библиотеку aiohttp, которая используется для создания асинхронных веб-приложений
from datetime import datetime  # Импортируем класс datetime для работы с датой и временем
from aiohttp.web_request import Request  # Импортируем класс Request из aiohttp, который представляет HTTP-запрос
from aiohttp.web_response import Response  # Импортируем класс Response из aiohttp, который используется для отправки HTTP-ответов
routes = web.RouteTableDef()  # Создаем объект, который будет хранить все маршруты веб-приложения (таблицу маршрутов)
@routes.get('/t') # Определяем асинхронную функцию, которая будет обрабатывать HTTP GET запросы на путь "/t"
async def time(request: Request) -> Response: # Функция time обрабатывает запросы по маршруту "/t" и возвращает ответ типа Response
    today = datetime.today()  # Получаем текущую дату и время с помощью datetime.today()
    for i in range(0,1000001): # Пустой цикл, который выполняет 1 миллион итераций (симулирует нагрузку или задержку)
        pass  # Это просто пустой блок, который не делает ничего, но используется для имитации работы программы
    result = {  # Формируем результат, который будет отправлен в виде JSON-ответа
    'month': today.month,
    'day': today.day,
    'time': str(today.time()), # Время текущей даты (без даты, только время)
    'message': 'Здравствуй, мир!'
}
    return web.json_response(result)  # Возвращаем объект `result` в виде JSON-ответа

@routes.get('/time') # Определяем асинхронную функцию, которая будет обрабатывать HTTP GET запросы на путь "/time"
async def time(request: Request) -> Response: # Функция time обрабатывает запросы по маршруту "/time" и возвращает ответ типа Response
    today = datetime.today() # Получаем текущую дату и время с помощью datetime.today()
    for i in range(0,1000001): # Пустой цикл, аналогично предыдущему
        pass  # Пустой блок для имитации работы программы
    result = {
    'month': today.month,
    'day': today.day,
    'time': str(today.time()),
    'message': 'Hello world!'
}
    return web.json_response(result)

app = web.Application() # Создаем объект приложения aiohttp
app.add_routes(routes) # Добавляем таблицу маршрутов `routes` к приложению (регистрация маршрутов)
web.run_app(app)   # Запускаем приложение на сервере, который будет слушать запросы на порту 8080 по умолчанию

