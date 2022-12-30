import pytest
from httpx import AsyncClient

from .main import app


@pytest.mark.anyio
async def list():
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        response = await ac.get("/list/1")
        assert response.status_code == 200
        assert response.json() == {"title":"Python", "price":500}
