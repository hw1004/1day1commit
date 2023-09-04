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

