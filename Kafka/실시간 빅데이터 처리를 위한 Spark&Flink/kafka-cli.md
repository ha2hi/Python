1. Zookeper 실행
`./bin/zookeeper-server-start.sh -daemon ./config/zookeeper.properties`

2. Kafka 브로커 실행
`bin/kafka-server-start.sh -daemon ./config/server.properties `

3. Topic 생성
`./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic first-topic --partitions 1 --replication-factor 1`

4. 프로듀서 생성
`./bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic`

5. 컨슈머 생성
`./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic`

6. 컨슈머 그룹 지정
`./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --group first-group`

- Command Tip
1. Topic 목록
`./bin/kafka-topics.sh --list --bootstrap-server localhost:9092`
2. Topic의 상세 정보
`./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092`
3. Consumer Group 목록
`./bin/kafka-consumer-group.sh --bootstrap-server localhost:9092 --list`
4. Consumer Group 상세 정보
`./bin/kafka-consumer-group.sh --bootstrap-server localhost:9092 --describe --group first-group`
5. 실행 유무 확인
`netstat -an | grep 2181`

Topic의 Partition 1개로 지정된 경우 Consumer Group에서 1개의 Consumer에게만 메세지가 전달된다. 
만약 Consumer Group에 다수의 Consumer가 있는 경우 Topic의 Partition 수를 늘려야 한다. 분산 처리 같은 할 때 Topic의 Patition 수는 중요하다.