# 제어문 (Control Statement)
- 코드 실생의 순차적인 흐름 제어(Control Flow)
- 제어문: 조건문, 반복문


# 조건문 (Conditional Statement)

## `if` 조건문
- 반드시 참/거짓을 판단할 수 있는 조건과 사용
- 조건이 참인 경우 수행하고 거짓인 경우 그 다음 if, elif, else문으로 넘어간다.
- else문은 선택적으로 사용
- 4spaces 유의!!

## `elif` 복수 조건
- 2개 이상의 조건 활용 경우
- `if`는 만약에라면 `elif`는 else if로 if가 성립 안될 판단되는 조건문이다.


## 중첩 조건문(Nexted Conditional Statement)
- 조건문은 다른 조건문에 중첩 가능

## 조건 표현식(Conditional Expression)
- 조건에 따라 값을 정할 때 사용됨
- `if-else`문에서만 적용된다.
- 조건식의 경우 bool값을 생각해서 값을 정함

```
1 if True else 0  # 1

# if와 else 사이가 조건문이다.

# 조건문이 True, 1,'asdf', 3 > 2와 같이 bool값이 True인 값들이면 if 앞에 오는 값을 정한다.
# 조건문이 False, 0, '', 3 < 2와 같이 bool값이 False인 값들이면 else 뒤에 오는 값을 정한다.
```