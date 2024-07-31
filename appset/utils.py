
import logging
from aiohttp import web
from playhouse.shortcuts import model_to_dict
from appset.models import (
    Device, 
    Location, 
    User
)



async def create_user(request):
    try:
        data = await request.json()
        logging.info(f"Creating user with data: {data}")
        user = await request.app['objects'].create(User, **data)
        logging.info(f"User created with ID: {user.id}")
        return web.json_response({'id': user.id})
    except Exception as e:
        logging.error(f"Error creating user: {e}")
        return web.json_response({'error': str(e)}, status=400)
    
async def get_devices(request):
    try:
        devices = await request.app['objects'].execute(Device.select())
        devices_list = [model_to_dict(device) for device in devices]
        logging.info(f"Retrieved {len(devices_list)} devices")
        return web.json_response(devices_list)
    except Exception as e:
        logging.error(f"Error retrieving devices: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def create_device(request):
    try:
        data = await request.json()
        logging.info(f"Creating user with data: {data}")
        device = await request.app['objects'].create(Device, **data)
        logging.info(f"Device created with ID: {device.id}")
        return web.json_response({'id': device.id})
    except Exception as e:
        logging.error(f"Error creating device: {e}")
        return web.json_response({'error': str(e)}, status=400)

async def update_device(request):
    try:
        device_id = int(request.match_info['device_id'])
        data = await request.json()
        logging.info(f"Updating device with ID {device_id} with data: {data}")
        await request.app['objects'].execute(Device.update(**data).where(Device.id == device_id))
        logging.info(f"Device with ID {device_id} updated successfully")
        return web.json_response({'status': 'success'})
    except Exception as e:
        logging.error(f"Error updating device with ID {device_id}: {e}")
        return web.json_response({'error': str(e)}, status=400)

async def delete_device(request):
    try:
        device_id = int(request.match_info['device_id'])
        logging.info(f"Deleting device with ID {device_id}")
        await request.app['objects'].execute(Device.delete().where(Device.id == device_id))
        logging.info(f"Device with ID {device_id} deleted successfully")
        return web.json_response({'status': 'success'})
    except Exception as e:
        logging.error(f"Error deleting device with ID {device_id}: {e}")
        return web.json_response({'error': str(e)}, status=400)
    
async def create_location(request):
    try:
        data = await request.json()
        logging.info(f"Creating location with data: {data}")
        location = await request.app['objects'].create(Location, **data)
        logging.info(f"Location created with ID: {location.id}")
        return web.json_response({'id': location.id}, status=201)
    except Exception as e:
        logging.error(f"Error creating location: {e}")
        return web.json_response({'error': str(e)}, status=400)
