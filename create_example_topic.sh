cd kafka_2.12-3.3.1
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic quickstart-events-1