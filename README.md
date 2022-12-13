# Custom kafka healtcheck plugin for site24x7
* Author : TechstyleOS
* In order to learn about JMX Service URLs and how to configure them, please refer to the following link: https://docs.oracle.com/cd/E19159-01/819-7758/gcnqf/index.html

## Description :
* This plugin monitors the health of kafka cluster. 
* The plugin will check the health of kafka cluster by connecting to 3 diffirent JMX ports of kafka cluster, kafka producer and kafka broker, see Kafka_Complete_Monitoring for examples.

## Prerequisites:
* Install the site24x7 linux agent on the server where the plugin is installed if on prod server.
* Install the python on the server where the plugin is installed.

## Installation:
* Download kafka from apache kafka by typing on base folder "bash install.sh".
* Install the python packages by typing "pip install -r requirements.txt" on the server where the plugin is installed.
* Place the plugin script at /opt/site24x7/monagent/plugins/kafka
* Configure the plugin by specifying the hosts, amd ports and the topic name using ".env" file. Create a .env file and write down like below example:
```
KAFKA_HOST=localhost
KAFKA_JMX_PORT=1999
KAFKA_CONSUMER_PARTITION=0
KAFKA_TOPIC_NAME=quickstart-events

ZOOKEPER_HOST=localhost
ZOOKEPER_JMX_PORT=9999
```
