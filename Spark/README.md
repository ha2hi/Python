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