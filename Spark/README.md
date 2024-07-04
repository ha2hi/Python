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