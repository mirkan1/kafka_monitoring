#!/usr/bin/python3
import json
import jmxquery as jmx

PLUGIN_VERSION = 1
HEARTBEAT = True
METRICS_UNITS = {
    "ISR Shrinks Per Sec":"sec",
    "ISR Expands Per Sec":"sec",
    "Leader Election Rate And Time Ms":"ms",
    "Unclean Leader Elections Per Sec":"sec",
    "Bytes In Per Sec":"sec",
    "Bytes Out Per Sec":"sec",
    "Network Request Rate":"sec",
    "Network Error Rate":"sec"
}

class KafkaBroker:
    def __init__(self, args):
        self.main_data={}
        self.main_data['plugin_version'] = PLUGIN_VERSION
        self.main_data['heartbeat_required']=HEARTBEAT
        self.main_data['units']=METRICS_UNITS

        self.kafka_host=args.kafka_host
        self.kafka_jmx_port=args.kafka_jmx_port
        self.kafka_consumer_partition=int(args.kafka_consumer_partition)
        self.kafka_topic_name=args.kafka_topic_name
        self.logsenabled=args.logs_enabled
        self.logtypename=args.log_type_name
        self.logfilepath=args.log_file_path

    def metric_collector(self):
        try:
            jmx_connection = jmx.JMXConnection(f"service:jmx:rmi:///jndi/rmi://{self.kafka_host}:{self.kafka_jmx_port}/jmxrmi")
            metric_queries = {
                "Under Replicated Partitions":"kafka.server:type=ReplicaManager,name=UnderReplicatedPartitions",
                "ISR Shrinks Per Sec":"kafka.server:type=ReplicaManager,name=IsrShrinksPerSec/Count",
                "ISR Expands Per Sec":"kafka.server:type=ReplicaManager,name=IsrExpandsPerSec/Count",
                "Active Controller Count" : "kafka.controller:type=KafkaController,name=ActiveControllerCount",
                "Offline Partitions Count" : "kafka.controller:type=KafkaController,name=OfflinePartitionsCount",
                "Leader Election Rate And Time Ms" : "kafka.controller:type=ControllerStats,name=LeaderElectionRateAndTimeMs/Count",
                "Unclean Leader Elections Per Sec" : "kafka.controller:type=ControllerStats,name=UncleanLeaderElectionsPerSec/Count",
                "Total Time Ms" : "kafka.network:type=RequestMetrics,name=TotalTimeMs,request=Produce/Count",
                "Purgatory Size":"kafka.server:type=DelayedOperationPurgatory,name=PurgatorySize,delayedOperation=Produce",
                "Bytes In Per Sec":"kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec/Count",
                "Bytes Out Per Sec":"kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec/Count",
                "Network Request Rate":"kafka.network:type=RequestMetrics,name=RequestsPerSec,request=Produce,version=9/Count",
                "Network Error Rate":"kafka.network:type=RequestMetrics,name=ErrorsPerSec,request=Produce,error=NONE/Count",
                "Total Broker Partitions":"kafka.server:type=ReplicaManager,name=PartitionCount/Value",
                "Young Generation GC Count":"java.lang:type=GarbageCollector,name=G1 Young Generation/CollectionCount",
                "Young Generation GC Time":"java.lang:type=GarbageCollector,name=G1 Young Generation/CollectionTime",
                "Old Generation GC Count":"java.lang:type=GarbageCollector,name=G1 Old Generation/CollectionCount",
                "Old Generation GC Time":"java.lang:type=GarbageCollector,name=G1 Old Generation/CollectionTime",
                f"Log End Offset(Partition : {self.kafka_consumer_partition})":f"kafka.log:type=Log,name=LogEndOffset,topic={self.kafka_topic_name},partition={self.kafka_consumer_partition}"
            }
            for key, value in metric_queries.items():
                jmx_query = [jmx.JMXQuery(value)]
                metric_result = jmx_connection.query(jmx_query)
                if len(metric_result) == 0:
                    continue
                self.main_data[key]=metric_result[0].value
            self.main_data["Topic Name"]=self.kafka_topic_name
            self.main_data["Partition No."]=f"Partition No : {self.kafka_consumer_partition}"

            applog = {}
            if(self.logsenabled in ['True', 'true', '1']):
                applog["logs_enabled"]=True
                applog["log_type_name"]=self.logtypename
                applog["log_file_path"]=self.logfilepath
            else:
                applog["logs_enabled"]=False
            self.main_data['applog'] = applog

        except Exception as err:
            self.main_data['msg']=str(err)
            self.main_data['status']=0
            return self.main_data

        return self.main_data

if __name__=="__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    kafka_host= os.environ.get("KAFKA_HOST") or "localhost"
    kafka_jmx_port= os.environ.get("KAFKA_JMX_PORT") or 1999
    kafka_consumer_partition= os.environ.get("KAFKA_CONSUMER_PARTITION") or 0
    kafka_topic_name= os.environ.get("KAFKA_TOPIC_NAME") or "quickstart-events"

    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--kafka_host', help='host name to access the kafka server metrics',default=kafka_host)
    parser.add_argument('--kafka_jmx_port', help='jmx port to access the kafka server metrics',default=kafka_jmx_port)
    parser.add_argument('--kafka_consumer_partition', help='partition to monitor the metrics',default=kafka_consumer_partition)
    parser.add_argument('--kafka_topic_name', help='kafka topic name',default=kafka_topic_name)

    parser.add_argument('--logs_enabled', help='enable log collection for this plugin application',default="False")
    parser.add_argument('--log_type_name', help='Display name of the log type', nargs='?', default=None)
    parser.add_argument('--log_file_path', help='list of comma separated log file paths', nargs='?', default=None)
    _args=parser.parse_args()

    obj=KafkaBroker(_args)

    result=obj.metric_collector()
    print(json.dumps(result, indent=4))
