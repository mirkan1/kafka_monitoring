export KAFKA_HEAP_OPTS="-Xms512m -Xmx4g"
export KAFKA_JMX_OPTS="-Dcom.sun.management.jmxremote=true \
                       -Dcom.sun.management.jmxremote.authenticate=false \
                       -Dcom.sun.management.jmxremote.ssl=false \
                       -Djava.rmi.server.hostname=127.0.0.1 \
                       -Dcom.sun.management.jmxremote.port=1999"
cd kafka_2.12-3.3.1
bin/kafka-server-start.sh config/server.properties