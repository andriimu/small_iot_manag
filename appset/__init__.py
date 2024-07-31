from aiohttp import web
from appset.routes import setup_routes 
from appset.models import (
    BaseModel, 
    init_db, 
    initialize_db
)


async def init_app():
    app = web.Application()
    await init_db(app)
    BaseModel._meta.database = app['db']
    initialize_db(app['db'])  
    setup_routes(app)
    return app