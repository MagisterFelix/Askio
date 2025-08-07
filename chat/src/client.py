from ollama import AsyncClient

from config import chat_settings

async_client = AsyncClient(host=chat_settings.URL)
