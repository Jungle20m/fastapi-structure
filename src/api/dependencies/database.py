
from typing import Generator
from src.database.database import engine


def get_connection():
    connection = engine.connect()
    return connection
    