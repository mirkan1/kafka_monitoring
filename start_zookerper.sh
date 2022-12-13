export JMX_PORT=9999
export KAFKA_HEAP_OPTS="-Xmx4G"
cd kafka_2.12-3.3.1
bin/zookeeper-server-start.sh config/zookeeper.properties