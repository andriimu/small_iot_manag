import asyncio
from aiohttp import web
from appset import init_app

if __name__ == '__main__':
    app = asyncio.run(init_app())
    web.run_app(app, port=8080)

    