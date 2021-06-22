import uvicorn
from fastapi import FastAPI

from src.core.config import SERVICE_NAME
from src.core.events import start_app_handler, stop_app_handler
from src.api.routes.api import router as main_router



app = FastAPI(title=SERVICE_NAME)

app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", stop_app_handler(app))

app.include_router(main_router, prefix="/structure")




if __name__ == '__main__':
    uvicorn.run("api_structure_main:app", host="192.168.10.152", port=6868, reload=True)