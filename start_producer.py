'''
    This script is equivalent to the following command:
    bash kafka_2.12-3.3.1/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic quickstart-events
'''
import os
from dotenv import load_dotenv
from kafka import KafkaProducer
load_dotenv()
server = f'{os.environ.get("KAFKA_HOST")}:{os.environ.get("KAFKA_JMX_PORT")}'
producer = KafkaProducer(
    security_protocol="PLAINTEXT",
    bootstrap_servers=["localhost:9092", "localhost:1999"], # cant connect to 1999
    client_id='console-producer',
)

import time
# run producer forever
while True:
    producer.send('quickstart-events', b'some_message_bytes')
    producer.flush()
    print("producer", producer.bootstrap_connected())
    time.sleep(5)
