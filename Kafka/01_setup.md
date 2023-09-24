# 1. Docker yaml file
docker-compose.yaml


```python
version: '3.1'
services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: ktech_zookeeper
    ports:
     - "2181:2181"
    restart: unless-stopped

  kafka:
    image: wurstmeister/kafka
    container_name: ktech_kafka
    ports:
     - "9092:9092"
    expose:
     - "9093"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: 'true'
      KAFKA_CREATE_TOPICS: "t1:1:1"
      KAFKA_LOG_RETENTION_HOURS: 1
      KAFKA_LOG_RETENTION_BYTES: 4073741824
      KAFKA_LOG_SEGMENT_BYTES: 1073741824
      KAFKA_RETENTION_CHECK_INTERVAL_MS: 300000
    volumes:
     - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
```

# 2. Docker compose
Execute :\
docker-compose up -d\

This command starts all services defined in the docker-compose in detached mode.

# 3. Verify running containes
docker ps

![docker_ps](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/kaafka/01_docker_ps.PNG?raw=true)

# 4. Create Topics
### 4.1 configure topic in yaml file:\
&nbsp;&nbsp;KAFKA_AUTO_CREATE_TOPICS_ENABLE: 'true'\
        you can just start using the broker and topics will be created as and when they're first referenced by the producer or consumer.\
        \
&nbsp;&nbsp;KAFKA_CREATE_TOPICS: "Topic1:1:3,Topic2:1:1:compact"\
        Topic 1 will have 1 partition and 3 replicas, Topic 2 will have 1 partition, 1 replica and a cleanup.policy set to compact.\
        

### 4.2 Use kafka-topics.sh
Move into Kafka container \
docker exec -it \<kafka_conatiner_id\> /bin/sh \
\
Go inside kafka installation folder \
cd /opt/kafka_<version>/bin  \
 \
Create Kafka topic \
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic quickstart



![create_topic](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/kaafka/02_create_topic.PNG?raw=true)

# 5 Start producer script:

kafka-console-producer.sh --topic t2 --bootstrap-server localhost:9092

# 6. Start Consumer script
To read from beginning: \
kafka-console-consumer.sh --topic t2 --from-beginning --bootstrap-server localhost:9092 \
\
        To read from current:\
            kafka-console-consumer.sh --topic t2 --bootstrap-server localhost:9092
    
        
    

![snap](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/kaafka/03_prod_consumer_interactive.PNG?raw=true)

# 7. producer.py and consumer.py

![produ](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/kaafka/04_producer_py.PNG?raw=true)

![consu](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/kaafka/05_consumer_py.PNG?raw=true)
