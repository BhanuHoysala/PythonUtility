# Bootstrapping Zookeeper and Kafka broker from python script with one click execution on Windows

import subprocess
import time

# ---------------- Starting Zookeeper ----------------

zookeeperPath = r'C:\Extended\Software\Kafka\kafka_2.12-2.2.0\bin\windows\zookeeper-server-start.bat'
zookeeperConfigFilePath = r'C:\Extended\Software\Kafka\kafka_2.12-2.2.0\config\zookeeper.properties'

zookeeperSubProcessCommand = zookeeperPath + " " + zookeeperConfigFilePath

print("Command being executed is \n" + zookeeperSubProcessCommand)
print("Bootstrapping Zookeeper")
subprocess.Popen('start ' + zookeeperSubProcessCommand, shell=True)
time.sleep(3)

# ---------------- Starting kafka Broker ----------------

kafkaPath = r'C:\Extended\Software\Kafka\kafka_2.12-2.2.0\bin\windows\kafka-server-start.bat'
KafkaConfigFilePath = r'C:\Extended\Software\Kafka\kafka_2.12-2.2.0\config\server.properties'

kafkaSubProcessCommand = kafkaPath + " " + KafkaConfigFilePath

print("Command being executed is \n" + kafkaSubProcessCommand)

print("Bootstrapping Kafka broker")
subprocess.Popen('start ' + kafkaSubProcessCommand, shell=True)
