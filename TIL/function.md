# 함수 (Function)
- **함수** : 특정한 기능을 하는 코드의 묶음
- **가독성** : 함수는 이해하기 쉬워야 한다
- 재사용성, 유지보수
- 함수는 비효율적이면 안된다.

```
def squaremeter(num):
    val = num ** 2
    return val
```
- *반드시* 하나의 값 반환 (return 값이 없으면 None을 반환)

## 함수 Output
- 함수는 어떠한 종류의 값과 상관없이 무조건 반환되는 값이 있다.
- **오직 한 개의 객체만 반환됨**
- 함수에 리턴이 없으면 자동으로 None이 리턴된다
```
def no_return():
    x = 1
    y = 2    # return 값이 없음

result = no_return()   # None
type(result)   # NoneType

# 따라서 이런 경우에도 None이 리턴되기 때문에 모든 함수는 리턴값이 있다.
```

## 함수 Input
- <span style="background-color:#fff5b1">**매개변수**</span> : 입력을 받아 함수 내부에서 사용하는 변수 (함수의 정의)
- <span style="background-color:#fff5b1">**전달인자**</span> : 실제로 전달되는 값 (함수의 호출)
- <span style="background-color:#fff5b1">**위치인자**</span> : 기본적으로 인자는 위치에 따라 순서대로 함수 내에 전달됨
- 함수는 입력값으로 인자를 넘겨줌
- <span style="background-color:#fff5b1">**기본 인자 값**</span> : 입력값이 없을 때 그 상황에서 사용될 값
```
def greeting(name='익명'):
    return f'{name}, 안녕?'

print(greeting()) 
# 이렇게 위치 인자가 생략되어 있으면 매개변수가 name만 있을 때는 error인데 매개변수에 name='익명'이라고 적을 시 익명, 안녕?으로 나온다.
```

- 하지만 기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없다.
```
# 예를 들면
def greeting(name='john', age):
    ~
# 이렇게는 사용 불가능하다.

greeting(20) 
#이렇게 호출할 시 첫번째 위치 인자로 인식되기 때문에 기본값이 있는 게 없는 것 앞에 올 수 없다.
```
- <span style="background-color:#fff5b1">**키워드 인자**</span> : 함수를 호출할 때 직접 변수의 이름으로 특정 인자 전달할 수 있게 함
```
greeting(name='정혜원', address='용인', age=20, major='통계')

# 순서에 상관없이 지정된 변수로 특정 인자 전달 가능
# 위치 인자와 같이 사용될 시 위치 인자는 순서대로, 키워드 인자는 지정한 인자
```
- 키워드 인자로 지정을 시작했으면 끝까지 키워드 인자를 사용하여야 한다.
- 키워드 인자 다음에 위치 인자를 활용할 수는 없다.


## 정해지지 않은 여러 개의 인자 처리
- 함수는 정해진 인자의 수가 있다.
- 하지만 `print` 함수는 그렇지 않아보인다.
- `print`처럼 정해지지 않은 임의의 인자를 받기 위해서는 **가변(임의) 인자 리스트** 를 사용한다.
- `*args` : 가변 인자 리스트
```
def func(a, b, *args)
# 보통 가변 인자 리스트는 매개변수 목록의 가장 마지막에 옴
```
- 가변 인자 리스트는 함수 내부에서 **tuple**형으로 사용됨
- `**kwargs`: 임의의 개수의 **키워드 인자**를 받음
  - (ex) `x=1, y=2, z=3` => dictionary 형태로 반환됨


# 함수 2
## 함수와 스코프
- **Global** (전역 스코프/ 변수): 어디서든지 참조 가능
- **Local** (지역 스코프/ 변수): 함수 내부에서만 참조 가능
- 지역에서 전역 변수 참조 가능
- 전역에서 지역 변수 참조 불가능
- 인자는 함수 내의 변수이다.
- **Built-in** (빌트인): lifecycle이 영원함

### LEGB Rule
- L : local scope (함수)
- E : Enclosed scope (상위 함수)
  - ```
    def func(name):   # enclosed
        def func2(n):   # local
    ```
- G : Global scope
- B : Built-in scope
  - built-in 함수는 값을 지정하면 안됨 그러면 global로 인지를 하게 되고 기존의 built-in 함수의 기능을 못하기 때문에 not callable error를 냄

### 전역 변수를 바꾸는 방법
- `global` 키워드를 사용해 local에서 global의 변수값을 변경할 수 있음.
```
num = 1
def local_scope():
    global num
    num = 100
    print('local?', num)

local_scope()

print(num)  # local에서 바꾼 값인 100 출력
```
- `global`, `nonlocal` : 상위 스코프의 변수 변경 (global - enclosed - local)

## 재귀 함수
- 함수 내에서 자기 자신을 호출 하는 함수 (알고리즘)
- 변수 사용을 줄여준다는 장점이 있다.
- 함수가 호출될 때마다 메모리 공간에 쌓이기 때문에 속도와 메모리 측면에서 단점이 있다. (입력값이 커질 수록 오래 걸림)
- 최대 재귀 깊이 : 재귀 함수가 1000번이 넘어가게 실행되면 종료함
- 재귀 함수를 사용할 때: 알고리즘에서 재귀적인 표현이 더 자연스러운 경우
- 속도: 반복문이 재귀보다 빠름


## map
```
list(map(int, ['1', '2', '3']))
```
- 순회 가능한 데이터 구조(['1', '2', '3'])의 모든 요소에 함수(int)를 적용하여 결과를 돌려줌
```
# list comprehension으로 비슷하게 구현 가능
[int(a) for a in ['1', '2', '3']]
```
- int 말고도 사용자가 정의한 다른 함수들도 map에 적용 가능함.


## filter
```
numbers = list(range(10))
def is_odd(num):
    return num % 2 != 0

list(filter(is_odd, numbers))
```
- 순회 가능한 데이터 구조(list(range(10)))의 모든 요소의 bool값을 판별하여 값이 True인 요소들만 반환


## lambda
- **기명 레인지**: r = range(10)의 r처럼 이름이 있다.
- **익명 레인지**: range(10) 처럼 이름이 지정되어 있지 않다.

- `lambda`함수 : 표현식 계산 결과 반환, 익명 함수라고도 불림
- return문을 가질 수 없음
- map과 filter 등을 사용하기 위해 함수를 직접 정의하는 경우 등의 상황에서 함수를 정의하지 않고 간결하게 사용 가능한 장점이 있다.
```
(lambda x, y: x + y)(1, 3)  # 4

list(map(lambda n: n ** 3, range(1, 20)))
```
- 위의 예시처럼 lambda를 붙여 이름 떼고도 사용 가능하다.