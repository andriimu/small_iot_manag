import peewee_async
from peewee import (
    Model, 
    CharField, 
    ForeignKeyField
)

config = {
    'database': 'iot_manager',
    'user': 'postgres',
    'password': 'postgres', 
    'host': 'localhost',
    'port': 5432
}

db = peewee_async.PooledPostgresqlDatabase(
        config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
    )



async def init_db(app):
    db = peewee_async.PooledPostgresqlDatabase(
        config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
    )
    objects = peewee_async.Manager(db)
    db.set_allow_sync(False)
    app['db'] = db
    app['objects'] = objects

    # Cleanup on shutdown
    async def close_db(app):
        await app['objects'].close()
    app.on_cleanup.append(close_db)



class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

class Location(BaseModel):
    name = CharField(unique=True)

class Device(BaseModel):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref='devices')
    api_user = ForeignKeyField(User, backref='devices')

def initialize_db(database):
    with database:
        database.create_tables([User, Location, Device])
