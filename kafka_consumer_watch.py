import time
import jmxquery

# Set the JMX connection parameters
jmx_url = 'service:jmx:rmi:///jndi/rmi://localhost:9983/jmxrmi'
jmx_user = None
jmx_password = None

# Create a JMX connection
connection = jmxquery.JMXConnection(jmx_url, jmx_user, jmx_password)

# Set the MBean object name prefix
object_name_prefix = 'kafka.consumer:type=consumer-fetch-manager-metrics,client-id='

# Set the attribute to retrieve
attribute = '*'

# Set the polling interval
poll_interval = 5

# Set the consumer group ID
consumer_group_id = 'console-consumer'

# Run the monitoring loop indefinitely
while True:
    # Set the MBean object name for the consumer group
    object_name = f'{object_name_prefix}{consumer_group_id}'

    # Create a JMX query
    query = [jmxquery.JMXQuery(object_name, attribute)]

    # Execute the JMX query
    result = connection.query(query)

    # Print the result
    metric = result[0]
    print(f'{metric.timestamp} {metric.value}')

    # Sleep for the polling interval
    time.sleep(poll_interval)
