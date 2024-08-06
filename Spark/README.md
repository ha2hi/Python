### Spark
---
빅데이터 처리를 위한 오픈소스 고속 분산처리 엔진  
1. 고속
- 메모리에서 실행
  - 기존의 MapReduce에 비해 왜 빠를까? MapReduce는 디스크에서 데이터를 읽고 처리하기 때문에 시간이 오래 걸렸으나, Spark는 메모리에서 처리하기 때문에 빠르다.
- Lazy Execution
  - Action 작업에서 한 번에 처리한다.
2. 분산처리
하나의 컴퓨터에서 처리하는 것이 아니라 데이터를 쪼개서 여러 노드에서 실행되기 때문에 속도가 빠르다.

### Spark Topology
Driver Program에서 Spark Context 오브젝트를 생성하고 작업을 실행하면 Cluster Manager(YARN, Mesos)를 통해 워커 노드애 보냅니다.  
워커 노드 안에 Executor에서 작업을 처리하고 결과를 Spark Context로 보냅니다.

### RDD(Resilient Distributed Dataset)
RDD는 스파크가 사용하는 핵심 데이터 모델이다. RDD를 이해하면 Spark를 이해할 수 있을 것이다.
1. 데이터 추상화
- 흩어져 있는 데이터를 하나의 데이터인 것 처럼 사용이 가능하다.
2. 불변성(Immutable)
- RDD는 불변하기 때문에 전처리 결과를 각각의 다른 RDD로 저장한다. 부득이한 장애가 발생시 복구가 편한다.
3. Type-safe
- 컴파일시 Type을 판별할 수 있어 문제를 일찍 발견할 수 있다.
4. 정형데이터(Structured Data) & 비정형데이터(Unstructured Data)
- 정형 데이터와 비정형 데이터 모두 담을 수 있다.
5. Lazy Execution
- Spark의 작업은 "Transformation"과 "Action"이 있다. Action을 만나면 Transformation을 전부 실행한다.
- 이렇기 때문에 디스크 접근을 줄일 수 있다.

### Cache & Persist
- 데이터를 메모리에 저장하고 싶을 때 사용할 수 있는 함수
- Cache
  - RDD : MEMORY_ONLY
  - DataFrame : MEMORY_AND_DISK
- Persist
  - Storage Level 지정하여 사용
- Storage Level
  - MEMORY_ONLY : 메모리에만 저장
  - MEMORY_AND_DISK : 메모리와 디스크에 저장
  - MEMORY_ONLY_SER : Serealize형태로 메모리에 데이터 저장(저장 용량에서 이점이 있지만 deSER과정이 필요하기 때문에 CPU 사용량 증가)
  - MEMORY_AND_DISK_SER
  - DISK_ONLY
- unpersist
  - 언캐싱

### 셔플링(Shuffling)
- 그룹핑시 데이터를 한 노드에서 다른 노드로 옮길 때 발생
- 그룹핑 시 많은 네트워크 연산이 이뤄짐(네트워크 연산)
- 다른 RDD 참조시
- 셔플링을 최소화 하려면
  1. 미리 파티션을 만들어 두고 캐싱 후 reduceByKey 실행  
      groupByKey를 하는 경우 셔플링을 전부 한 이후에 값을 합치지만, reduceByKey를 사용하는 경우 값을 먼저 합치고 셔플링 작업이 일어나기 때문에 groupByKey보다 상대적으로 네트워크 연산이 작다.
  2. 미리 파티션을 만들어 두고 캐싱 후 Join 실행

### 파티션(Partition)
파티션의 목적
- 데이터를 최대한 균일하게 퍼트리고 쿼리가 같이 되는 데이터를 최대한 옆에 두어 검색 성능을 향상시키는 것

특징
- RDD는 쪼개져서 여러 파티션에 저장
- 하나의 파티션은 하나의 노드(서버)에 저장
- 하나의 노드는 여러개의 파티션을 가질 수 있음
- 파티션의 크기와 배치는 자유롭게 설정 가능하며 성능에 큰 영향을 미침
- Key-Value RDD를 사용할 때만 파티션의 의미가 있음(Hash 검색을 통해 빠르게 찾을 수 있기 때문)
- 파티션을 만든 후에 persists()하지 않으면 연산 불릴 때 마다 반복하게 된다.

종류
- Hash partitioning : 데이터를 여러 파티션에 균일하게 분배
- Range Partitioning : 순서가 있고 정렬된 파티셔닝

파티션 방법
```
pairs = sc.parallelize([1,2,3,4,2,4,1]).map(lambda x : (x,x))
paris.partitionBy(2).glom().collect()

paris.partitionBy(2, lambda x : x%2).glom().collect()
```

- Repartition vs Coalesce
- Repartition : 파티션의 크기를 줄이거나 늘리는데 사용됨
- Coalesce : 파티션을 줄이는데 사용됨
  
### Catalyst & Tungsten
스파크는 쿼리를 돌리기 위해 Catalyst와 Tungsten엔진을 사용한다.
SQL, DataFrame -> Query Plan Optimization(Catalyst) -> RDD(Tungsten)

1. Catalyst: Logical Plan -> Physical Plan으로 변환 역할을한다.
- Logical Plan
  - 모든 Transformation 단계에 대한 추상황
  - 데이터를 어떻게 변환할지는 정의하지만 실제 어디서 동작하는지는 정의하지 않음
- Physical Plan
  - Logical Plan이 어떻게 클러스터 위에서 실행될지 정으
- Catalyst 실행 순서
  - 1.분석 : DataFrame 객체의 Relation 계산, 컬럼의 타입과 이름 확인
  - 2.Logical Plan 최적화
    - 상수로 표현된 표현식을 Compile time에 계산
    - Predicate Pushdown : Join & Filter -> Filter & Join
    - Project Pruning : 연산에 필요한 컬럼만 가져오기
  - 3.Physical Plan 생성
    - 스파크에서 실행 가능한 Plan으로 변환
  - 4.코드 제너레이션
    - 최적화된 physical Plan을 Java Bytecode로 변환

2. Tungsten
- Physical Plan을 분산 환경에서 실행할 ByteCode를 만든다.(Code Generation)
- 스파크 엔진의 성능 향상 목적
  - 메모리 관리 최적화
  - 캐시 활용 연산
  - 코드 생성
  
### Spark Streaming
- SQL 엔진 위에 만들어진 분산 스트림 처리 프로세싱
- 데이터 스트림(무한한 데이터)을 처리할 때 사용
- 시간대 별로 데이터를 합쳐(aggregate) 분석할 수 있음
- Kafka, AWS Kinesis, HDFS 등과 연결 가능
- 체크포인트를 만들어서 부분적인 결함이 발생해도 다시 돌아가서 데이터를 처리할 수 있음
- 무한한 데이터를 쪼개서 처리한다.
- 이전 데이터에 대한 정보를 State로 주고받을 수 있음

### 참고하면 좋은 블로그
https://1ambda.gitbook.io/practical-data-pipeline/02-processing/2.2-batch/2.1.1-spark-intro
