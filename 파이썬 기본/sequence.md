### Sequence란?
Sequence는 파이썬 추상 베이스 클래스(Abstract Base Class, ABC) 중 하나로, list, tuple, str, range 등 처럼 순서가 있고, 인덱싱 가능한 객체를 의미합니다.  
즉, Sequence는 시퀀스 자료형의 공통 인터페이스를 정의한 것 입니다.  

### 사용 목적
1. 타입 힌트  
```
from collections.abc import Sequence

def print_items(items: Sequence[str]):
    for item in items:
        print(item)

print_items(["apple", "banana"])  # ✅ OK
print_items(("x", "y", "z"))      # ✅ OK
print_items("hello")              # ✅ OK (문자열도 시퀀스)
print_items(123)                  # ❌ TypeError
```  
2. isinstance 검사  
```
from collections.abc import Sequence

data = [1, 2, 3]

if isinstance(data, Sequence):
    print("시퀀스 타입입니다.")
```
