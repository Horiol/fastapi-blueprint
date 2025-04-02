# broker.py
from .constants import REDIS_FASTSTREAM_DB
from faststream import FastStream
from faststream.redis import RedisBroker

broker = RedisBroker(f"redis://redis:6379/{REDIS_FASTSTREAM_DB}")
app = FastStream(broker)


@broker.subscriber("in-channel")
@broker.publisher("out-channel")
async def handle_msg(user: str, user_id: int) -> str:
    print("TEST")
    return f"User: {user_id} - {user} registered"
