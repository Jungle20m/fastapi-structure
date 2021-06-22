from typing import Callable
from typing import Callable

from fastapi import FastAPI

from src.helper import redis_handler


def start_app_handler(app: FastAPI) -> Callable:
    async def start_app():
        print("app started")
    return start_app

def stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app():
        print("app stoped")
    return stop_app