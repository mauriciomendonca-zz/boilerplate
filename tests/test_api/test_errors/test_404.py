import pytest
from httpx import AsyncClient
from starlette.status import HTTP_404_NOT_FOUND

pytestmark = pytest.mark.asyncio


async def test_error_404(client: AsyncClient):
    response = await client.get("/path/does/not/exist")
    assert response.status_code == HTTP_404_NOT_FOUND
