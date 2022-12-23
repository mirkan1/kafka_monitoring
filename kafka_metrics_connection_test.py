import os
from dotenv import load_dotenv
from jmxquery import JMXConnection, JMXQuery
load_dotenv()
kafka_consumer_host= os.environ.get("KAFKA_HOST") or "localhost"
kafka_consumer_jmx_port= os.environ.get("KAFKA_JMX_PORT") or 1999
kafka_consumer_partition= os.environ.get("KAFKA_CONSUMER_PARTITION") or 0
kafka_topic_name= os.environ.get("KAFKA_TOPIC_NAME") or "quickstart-events"

def printMetrics(metrics):
    for metric in metrics:
        if metric.metric_name:
            print(f"{metric.metric_name}<{metric.metric_labels}> == {metric.value}")
        else:
            print(f"{metric.to_query_string()} ({metric.value_type}) = {metric.value}")

    print("===================\nTotal Metrics: " + str(len(metrics)))

jmxConnection = JMXConnection(f"service:jmx:rmi:///jndi/rmi://{kafka_consumer_host}:{kafka_consumer_jmx_port}/jmxrmi")
jmxQuery = [JMXQuery("*:*")]
metrics = jmxConnection.query(jmxQuery)
printMetrics(metrics)
