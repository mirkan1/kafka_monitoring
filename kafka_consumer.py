import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
load_dotenv()
server = f'{os.environ.get("KAFKA_HOST")}:{os.environ.get("KAFKA_JMX_PORT")}'
consumer = KafkaConsumer(
    'quickstart-events',
    security_protocol="PLAINTEXT",
    bootstrap_servers="localhost:9092",
    client_id='console-consumer',
    group_id='console-consumer',
)
print("consumer", consumer.topics())
for msg in consumer:
    print(msg)
