cd kafka_2.12-3.3.1
export JMX_PORT=9984 
JMX_PORT=9984 
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic quickstart-events-1 --group console-consumer
