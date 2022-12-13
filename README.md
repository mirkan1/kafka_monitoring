# Custom kafka healtcheck plugin for site24x7
* Author : TechstyleOS
* In order to learn about JMX Service URLs and how to configure them, please refer to the following link: https://docs.oracle.com/cd/E19159-01/819-7758/gcnqf/index.html

## Description :
* This plugin monitors the health of kafka cluster. 
* The plugin will check the health of kafka cluster by connecting to the zookeeper.
* The plugin will check the status of the kafka cluster by executing the command "echo ruok | nc localhost 2181".
* The plugin will check the status of the kafka cluster by executing the command "echo stat | nc localhost 2181".
* The plugin will check the status of the kafka cluster by executing the command "echo mntr | nc localhost 2181".

## Prerequisites:
* Install the site24x7 linux agent on the server where the plugin is installed.
* create a .env file as write down like below example:
```
KAFKA_HOST=localhost
KAFKA_JMX_PORT=1999
KAFKA_CONSUMER_PARTITION=0
KAFKA_TOPIC_NAME=quickstart-events

ZOOKEPER_HOST=localhost
ZOOKEPER_JMX_PORT=9999
```

## Installation:
* Download kafka from apache kafka by typing on base folder "bash install.sh".
* Install the python packages by typing "pip install -r requirements.txt" on the server where the plugin is installed.
* Place the plugin script at /opt/site24x7/monagent/plugins/kafka
* Install the python on the server where the plugin is installed.
* Configure the plugin by specifying the zookeeper host, zookeeper port and the topic name using ".env" file.
