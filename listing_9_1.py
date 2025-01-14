from aiohttp import web
from datetime import datetime
from aiohttp.web_request import Request
from aiohttp.web_response import Response
routes = web.RouteTableDef()
@routes.get('/t')
async def time(request: Request) -> Response:
    today = datetime.today()
    for i in range(0,1000001):
        pass
    result = {
    'month': today.month,
    'day': today.day,
    'time': str(today.time()),
    'message': 'Здравствуй, мир!'
}
    return web.json_response(result)

@routes.get('/time')
async def time(request: Request) -> Response:
    today = datetime.today()
    for i in range(0,1000001):
        pass
    result = {
    'month': today.month,
    'day': today.day,
    'time': str(today.time()),
    'message': 'Hello world!'
}
    return web.json_response(result)

app = web.Application()
app.add_routes(routes)
web.run_app(app)
