from aiohttp import web
from appset.utils import (
    create_device, 
    create_location, 
    create_user, 
    delete_device, 
    get_devices, 
    update_device
)


def setup_routes(app):
    app.router.add_post('/users', create_user)
    app.router.add_get('/devices', get_devices)
    app.router.add_post('/devices', create_device)
    app.router.add_post('/locations', create_location)
    app.router.add_put('/devices/{device_id}', update_device)
    app.router.add_delete('/devices/{device_id}', delete_device)
