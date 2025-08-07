from fastapi import FastAPI

from src.views.message import router as message_router

app = FastAPI()
app.include_router(message_router)
