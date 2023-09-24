import json
from datetime import datetime
from time import sleep
from random import randint
from kafka import KafkaProducer

kafka_server = ["localhost"]

topic = "t2"

producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


while True:
    data = {
        "temperature" : randint(25,35),
        "timestamp": str(datetime.now()),
        }
    print(data)
    producer.send(topic, data)
    producer.flush()
    sleep(5)