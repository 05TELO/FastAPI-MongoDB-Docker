import json

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient
from api.config_data.config import load_config
from api.config_data.dirs import DIR_API
from api.config_data.dirs import DIR_REPO

conf = load_config(str(DIR_REPO / ".env"))

with open(str(DIR_API / "templates.json"), "r") as file:
    data = json.load(file)


client: AgnosticClient = AsyncIOMotorClient(conf.mongo.db_url)

db = client[conf.mongo.db_name]

collection = db[conf.mongo.db_col]

collection.insert_many(data)
