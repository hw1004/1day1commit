# 반복문 (Loop Statement)

## While 반복문 (수동)
- 조건식이 참일 경우 반복적으로 코드 실행
- 항상 True인 조건문을 설정할 경우 무한루프가 발생하므로 **종료조건**을 설정해야 함
```
while True:
    print('조건식이 참일 때')
    print('계속 반복')
```

## for ... in 구문 (자동)
- 리스트나 문자열의 요소들이 처음부터 끝까지 차례로 임시변수에 할당됨
- ```
  for <임시변수> in <순회가능한데이터>:
      <코드 블럭>
  ```
- 정해진 시퀀스 내에서의 반복 시 사용
- 순회가능한데이터의 모든 것을 조회한다.

 **딕셔너리 순환**
- ```
  grades = {'john': 80, 'eric': 90}
  
  # values 값을 출력할 때
  for key in grades:
      print(grades[key])
  ```
- key에 접근 가능하면 value에도 접근 가능
- `.keys()`, `.values()`, `.items()`으로 활용 가능
- `.items()`는 튜플들로 이루어져 있기 때문에 임시변수에서도 tuple 할당 가능
- ```
  for key, val in grades.items():
      print(key, val)
  ```


**enumerate()**
- 인덱스와 값(index and value)
- 인덱스와 값은 튜플 형태로 출력됨
- 리스트의 원소에 순서값을 부여해주는 내장 함수임.
- ```
  members = ['민수', '영희', '철수']
  
  for idx, val in enumerate(members):
      print(idx, val)
  ```
  ```
  # 인덱스를 0이 아닌 1이나 다른 숫자를 시작점으로 설정할 떄

  for idx, val in enumerate(members, start = 1):
       print(idx, val)
  ```

**List Comprehension**
- 리스트 만드는 과정 한 줄로 요약
```
numbers = [1, 2, 3]
cubic_list = []

for idx in range(len(numbers)):
    cubic_list.append(numbers[idx] **3)

print(cubic_list)


# List Comprehension으로 표현

numbers = [1, 2, 3]

cubic_list = [num ** 3 for num in numbers]

print(cubic_list)
```
- 임시변수에 값을 전혀 사용하지 않는다면, _로 쓰자!


**Dictionary Comprehension**
- dict 생성 과정 한 줄로 요약
```
cubic_dict = {}

for i in range(1, 4):
    cubic_dict[i] = i ** 3
print(cubic_dict)


# dictionary comprehension으로 표현

cubic_dict = {i: i ** 3 for i in range(1, 4)}

print(cubic_dict)
```

## 반복제어 (break, continue, for-else)

**break**
- 반복문(for, while)  종료
- break를 쓰면 해당하는 반복문이 반복을 중단하는 것
- 따라서 break 위치가 중요하다

**continue**
- continue 이후의 코드는 수행하지 않고 for문의 첫번째로 돌아가 다음 요소부터 계속하여 반복 수행

**pass**
- 아무것도 안함
- 들여쓰기 이후 자리를 채우는 용도로 사용
- 프로그램이 특별히 할 일이 없을 때 사용

## for-else문
- 반복문 끝까지 실행한 후 실행됨
- break문이 사용되지 않았다면 효력 없음(쓰는 의미가 없음음)
- 반복문이 중간에 만약 break문으로 종료되면 else문은 실행 X
- break에 걸리지 않고 다 실행했을 경우 else문의 코드 블록 출력
```
for char in 'banana':
    if char == 'b':
        print('b!')
        break
else:                    # b가 있으면 앞의 break가 끝나서 뒤에 실행 안됨
    print('b가 없습니다.')       # 중간에 break 없이 끝까지 수행한다면 else 붙임
```