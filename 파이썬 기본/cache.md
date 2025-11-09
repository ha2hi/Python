파이썬 내장 함수인 functools 내 cache, lru_cache를 통해 Python에서 함수의 실행 결과를 메모리에 저장해두고, 같은 인자로 다시 호출할 때 계산 없이 즉시 결과를 반환하도록 설정할 수 있다.  

## Cache
아래와 같은 상황에서 Cache를 사용하는 경우 속도를 개선할 수 있음.  
### 1. 계산 비용이 큰 함수
```
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

### 2. I/O난 객체 생성 비용이 큰 경우
```
from functools import cache
import json
import time

@cache
def load_config():
    print("loading config...")
    return json.load(open("test.json"))

# 첫 번째 호출
start = time.perf_counter()
load_config()
print("첫 번째 호출:", time.perf_counter() - start, "초")

# 두 번째 호출
start = time.perf_counter()
load_config()
print("두 번째 호출:", time.perf_counter() - start, "초")
```

### 3. 불변 인자에 대해 결과가 반복적으로 재사용되는 경우
```
from functools import cache

@cache
def parse_template(template: str):
    return compile_template(template)
```
인자가 계속 달라지는 경우 캐시가 계속 쌓이기 때문에 메모리 문제가 발생할 수 있음.  
이 때 lru_cache를 통해 메모리 관리하여 캐시 기능을 사용할 수 있음.  

## lru_cache
lru는 Least Recently Used의 약어로 자주 사용되는 데이터를 보유하고 가장 최근에 사용되지 않은 데이터를 삭제하여 메모리 관리함.  
```
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

## 그외 기능
### cache_info
cache_info를 통해 캐시 히트 및 미스를 확인할 수 있습니다.  
```
load_config.cache_info()

CacheInfo(hits=2, misses=1, maxsize=None, currsize=1)
```
=> 첫 번째 호출 때 캐시에 없어 직접 계산, 두 번째 호출 부터 캐시가 있어 즉시 반환

### cache_clear
캐시된 모든 결과를 지움.
```
load_config.cache_clear()

load_config.cache_info()
```
