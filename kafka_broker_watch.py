import time
import jmxquery

# Set the JMX connection parameters
jmx_url = 'service:jmx:rmi:///jndi/rmi://localhost:1999/jmxrmi'
jmx_user = None
jmx_password = None

# Create a JMX connection
connection = jmxquery.JMXConnection(jmx_url, jmx_user, jmx_password)

# Set the MBean object name to query
object_name = 'kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec'

# Set the attribute to retrieve
attribute = 'Count'

# Set the polling interval
poll_interval = 5

# Run the monitoring loop indefinitely
while True:
    # Create a JMX query
    query = [jmxquery.JMXQuery(object_name, attribute)]

    # Execute the JMX query
    result = connection.query(query)

    # Extract the attribute value from the result
    end_result = result[0].to_string()

    # Print the attribute value
    print(f'Final result it: {end_result}')
    
    # Sleep for the polling interval
    time.sleep(poll_interval)