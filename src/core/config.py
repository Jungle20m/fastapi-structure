import os
import json
import pickle

from starlette.config import Config

config = Config(".env-dev")

SERVICE_NAME = config("SERVICE_NAME") 

DB_NAME = config("DB_NAME")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT", cast=int)
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")

POOL_SIZE = config("POOL_SIZE", cast=int, default=5)