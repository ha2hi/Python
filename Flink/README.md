### 스트림 프로세싱
- 스트림 데이터는 데이터가 무한하다라는 가정하에 데이터를 처리
- 데이터가 도착할 때 마다 바로 처리
- 실시간으로 실행되는 작업
- 처리량보다는 처리속도가 중요

### Apache Flink
- 스트림 데이터 처리를 위한 프레임워크
- 분산처리/고성능/고가용성
- 배치 프로세싱 또한 지원
  - 배치 프로세싱도 지원하지만 스트리밍에 최적화된 프레임워크
- in-memory 방식
  - 메모리 위에서 작업을 처리하기 때문에 빠르다.
- Lazy Execution
  - Spark와 동일하 Action시 모든 작업을 처리한다.

### Flink 프로그래밍 모델
- Source -> Operation&Transformation -> Sink

### State란?
- 발생하는 여러 Event들을 한꺼번에 보려고 할 때 State가 필요하다.
- 예를 들어 패턴을 찾는 경우, 시간별로 합계, 머신러닝 트레이닝
- Key-value 데이터를 갖는 Event 데이터에서 Key 별 합계를 구하고 싶다면 key state를 사용한다.
- checkpoints와 savepoints로 state를 저장해서 내결함성을 갖도록 설계되었다.
- Data Stream API를 사용할 때 여러가지 경우로 state를 사용하게 된다.
  - Window로 데이터 모아보기
  - Transformations(key-value state)
  - CheckpointFunction으로 로컬 변수를 fault tolerant하게 만들기

### State Backend
Flink에서 State 방식으로 2가지 방식이 있다.
- HashMapStateBackend
  - Java Heap에 저장
  - Hash Table에 변수와 trigger저장
  - 큰 state, 긴 window, 큰 key-value 쌍을 저장할 때 권장
  - 고가용성 환경
  - 메모리 사용으로 빠른 처리
- EmbeddedRocksDBStateBackend
  - Flink 내장 DB인 RocksDB에 저장
  - 데이터는 byte array로 Serialize되어 저장
  - 매우 큰 state, 긴 window, 큰 key-value state 저장
  - 고가용성 환경
  - Disk와 Seriallize 사용하여 처리량은 높지만 성능은 떨어진다.

### Checkpoint
- 장애 허용 가능하게 해주는 기능
- 가벼운 state를 가진 프로그램은 자주 저장해도 된다.
- 시스템이 고장난 경우 Flink는 작동을 멈추고 CheckPoint 지점으로 리셋한다.

### Barriers
- 데이터를 시간별로 나누는 barrier를 삽입해 snapshot이 가능하다.
- barrier는 가벼워서 스트림에 방해되지 않도록 설계되었다.
- Sink Operator가 barrier를 받아서 새로운 checkpoint를 만든다.
베리어와 state를 저장하는걸 Snapshot이라 한다.

### 스트림 데이터 Time 종류
1. Processing Time
- 데이터를 처리하는 시스템의 시간
- 예를 들어 Hourly time window의 경우 11시 20분에 시스템 시작했다고 가정하면 11:20~12:00, 12:00~13:00 데이터처리
- 빠르고 Latency가 낮지만 Event가 시스템에 도달하는 속도에 달렸기 때문에 분산되고 비동기적인 환경에서는 결정적(deterministic)하지 못하다.
2. Event Time
- Event가 생성된 곳에서 만들어진 시간
- Event 자체에 기록 보관
- 시간은 시스템이 아닌 Data에 의존
- 여러 input stream을 받는 경우 상대적으로 낮은 event time을 사용