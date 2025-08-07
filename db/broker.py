from faststream.rabbit import RabbitBroker

from config import mq_settings

rabbit_broker = RabbitBroker(mq_settings.URL)
