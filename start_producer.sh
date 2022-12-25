cd kafka_2.12-3.3.1
export JMX_PORT=9982 
JMX_PORT=9982 
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092