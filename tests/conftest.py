import asyncio
from contextlib import closing

import pytest
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    with closing(policy.new_event_loop()) as loop:
        loop.set_debug(enabled=True)
        yield loop


@pytest.fixture
async def client():
    async with AsyncClient() as client:
        yield client
