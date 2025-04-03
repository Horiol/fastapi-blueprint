from faststream.redis.fastapi import RedisRouter, Logger

from src.constants import REDIS_FASTSTREAM_DB

router = RedisRouter(
    f"redis://redis:6379/{REDIS_FASTSTREAM_DB}",
)


@router.subscriber(stream="test-stream")
@router.publisher("response")
async def hello(m: dict, logger: Logger):
    logger.info(m)
    return {"response": "Hello, Redis!"}
