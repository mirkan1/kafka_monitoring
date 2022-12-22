export JMX_PORT=1999
export KAFKA_HEAP_OPTS="-Xms512m -Xmx2g"
cd kafka_2.12-3.3.1
bin/kafka-server-start.sh config/server.properties