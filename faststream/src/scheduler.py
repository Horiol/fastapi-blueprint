from .constants import REDIS_FASTSTREAM_DB
from faststream.redis import RedisBroker
from taskiq_faststream import BrokerWrapper
from taskiq_faststream import StreamScheduler
from taskiq.schedule_sources import LabelScheduleSource

broker = RedisBroker(f"redis://redis:6379/{REDIS_FASTSTREAM_DB}")
taskiq_broker = BrokerWrapper(broker)


taskiq_broker.task(
    message={"user": "John", "user_id": 1},
    channel="in-channel",
    schedule=[
        {
            "cron": "* * * * *",
        }
    ],
)

scheduler = StreamScheduler(
    broker=taskiq_broker,
    sources=[LabelScheduleSource(taskiq_broker)],
)
