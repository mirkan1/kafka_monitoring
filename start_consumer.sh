cd kafka_2.12-3.3.1
export JMX_PORT=9983 
JMX_PORT=9983 
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic quickstart-events --group console-consumer