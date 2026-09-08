# utils/api.py
import aiohttp
import os

# TODO: API_URL берётся из .env
API_URL = os.getenv("API_URL", "http://localhost:8000")

async def api_get(path: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}{path}") as resp:
            return await resp.json()
