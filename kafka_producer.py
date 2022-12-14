import os
from dotenv import load_dotenv
from kafka import KafkaProducer
load_dotenv()
server = f'{os.environ.get("KAFKA_HOST")}:{os.environ.get("KAFKA_JMX_PORT")}'
print("server", server)
producer = KafkaProducer(
    security_protocol="PLAINTEXT",
    bootstrap_servers="localhost:9092",
    client_id='console-producer',
)
for _ in range(100):
    producer.send('quickstart-events', b'some_message_bytes')
producer.flush()
print("producer", producer.bootstrap_connected())

# import time
# # run producer forever
# while True:
#     producer.send('quickstart-events', b'some_message_bytes')
#     producer.flush()
#     time.sleep(3)
