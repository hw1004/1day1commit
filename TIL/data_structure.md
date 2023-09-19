# 데이터 구조 (Data Structure)
- 자료 구조라고도 불림
- 데이터 접근의 효율성 가능케하는 데이터 구성, 관리, 저장형식
1. 데이터 값들
2. 해당 값들의 관계
3. 적용할 수 있는 함수와 명령어 모음


|순서 O|순서 X|
|---|---|
|문자열|셋|
|리스트|딕셔너리|
|튜플|

## 순서가 있는 데이터 구조
### 1. 문자열
- 변경 불가능(조회, 탐색만 가능)
- 순서 있음
- 순회 가능

`.find(x)` : x의 첫번째 위치 반환
- x가 발견되지 않으면 -1 반환

`.index(x)` : x의 첫번째 위치 반환
- x가 발견되지 않으면 오류

`.startswith(x)`, `.endswith(x)` : 문자열이 x로 시작되거나 끝나면 True 반환, 아니면 False 반환

- is~ 메서드들 : 문자열이 어떤 조건에 해당하는지 검증
- (ex) `.islower()`: 문자열이 전체 소문자로 이루어져 있는지 검증
- (ex) `.isspace()`: 순전히 공백으로 이루어진 문자열인지 검증(\n, \t도 공백으로 친다.)

#### 변경 (원본이 변경되지는 X)

`.replace(old, new, count)`: old를 new로 바꿈 (count는 old가 같은게 여러 개 있을 때 바꿀 개수를 정함)
- (ex) `a.replace('y', 'h')` => a가 직접적으로 바뀌는 것이 아니다. replace문 전체를 b라고 정의한다면 b라는 새로운 문자열이 생성된 것이다.

`.strip([chars])`: 특정한 문자를 지정하면 양쪽 제거
`.lstrip([chars])`, `.rstrip([chars])`: 왼쪽, 오른쪽 제거 / chars 지정 안하면 공백 제거
- (ex) 'hihihahahihi'라는 문자열에 `문자열.lstrip('hi')` 계산하면 'hahahihi'

`.split([chars])`: 문자열을 단위로 나누어 리스트로 반환
- (ex) 'a s d'.split()하면 ['a', 's', 'd']가 나옴
- 붙어있는 문자열을 한 글자씩 리스트로 만들고 싶으면 `list(string)`을 사용하면 됨
  
`.separator.join(iterable)`: seperator(구분자)로 이어붙인 문자열 반환함
- 문자열의 경우 글자끼리 구분자로 이어 붙임
- list의 경우 각 요소끼리 구분자로 이어 붙임

|`.capitalize`|`.title()`|`.upper()`|`.lower()`|`.swapcase()`|
|---|---|---|---|---|
|앞글자 대문자로 만듦|(') 또는 공백 이후를 대문자로 만듦|모두 대문자로 만듦|모두 소문자로 만듦|대,소문자 변경하여 반환|

`dir('')`: 문자열에 사용할 수 있는 메서드를 확인하는 방법

### 2. 리스트
- 변경 가능
- 순서 있음
- 순회 가능

#### 원본 변경
`.append(x)`: list에 x의 값을 추구한다.
- 리스트는 mutable하기 때문에 메서드를 사용하면 원본 자체가 변경된다. (return X)

`.extend(iterable)`: 리스트에 list, range, tuple, string 값을 추가할 수 있음
```
cafe.extend(['wcafe', '이디야'])   
# cafe list에 'wcafe', '이디야' 추가됨
```
- 원본이 변경되기 때문에 `+=`과 같은 역할을 한다고 보면 됨
- append vs extend
```
# 문자열을 넣었을 때

a.append('apple')
# append는 'apple' 전체가 list a에 추가됨

a.extend('apple')
# extend는 'a', 'p', 'p', 'l', 'e'가 차례대로 list에 추가됨
```

`.insert(i, x)`: index 위치 i에 x를 삽입한다.
```
# list의 가장 앞에 삽입
a.insert(0, x)

# list의 마지막에 삽입
a.insert(len(a), x)
# len(a)보다 큰 어떤 값(10000000)이 와도 마지막에 삽입됨
# a.append(x)와 같은 역할
```

`.remove(x)`: list에서 x 값 삭제(가장 첫번째로 오는)
- 반복으로 사용할 시 두번째, 세번째...로 오는 x의 값도 삭제 가능
```
numbers = [1, 2, 3, 1, 2]
numbers.remove(1)
numbers     # [2, 3, 1, 2]
```
- 삭제하려는 x의 값이 더 이상 list에 없으면 오류 발생


`.pop(i)`: index i번째에 위치한 값을 삭제하고 동시에 삭제된 값을 리턴
```
numbers = [1, 2, 3, 4, 5, 6]

numbers.pop(0)    # 1

numbers   # [2, 3, 4, 5, 6]

numbers.pop()     # 6

numbers   # [2, 3, 4, 5]
```
- i가 지정이 안되면 기본적으로 마지막 것을 삭제


`.clear()`: 리스트의 모든 항목 삭제
- `list = []`처럼 빈 리스트를 지정하는 방식과 리스트의 모든 항목을 삭제하는 `.clear()` 방식은 다름 (새로운 것을 만드느냐/ 기존에 있던 것을 지우느냐 차이)

#### 탐색, 정렬
`.index(x)`: x값의 인덱스 값 반환
- 찾는 값이 list에 없으면 오류 발생


`dir([])`: list에 사용되는 메서드 종류 반환
`help([])` or `help(list)`: list에 사용되는 메서드의 종류와 어떻게 사용되는지까지 상세히 반환

`.count(x)`: list 안에 x의 개수 반환

`.sort()`: 리스트 정렬 (원본 변형, None return - list를 다시 불러보면 정렬되어 출력됨)
```
lucky = [2, 1, 5, 3]
lucky.sort()  # 아무것도 반환 X
lucky # [1, 2, 3, 5]
```

- 내림차순 정렬을 하려면 `lucky.sort(reverse=True)`
- `sorted(lucky)`는 함수이기 때문에 정렬된 값을 return하고 원본이 변경되지는 않는다.
- 반면에 `.sort()`는 메서드이고 정렬된 값을 return하지 않고 원본이 변경된다.
- `sorted()`의 메모리 사용량이 더 많음.
#### dictionary에서 특정 key를 중심으로 정렬하는 방법!!!!!!!!!
```
# students라는 딕셔너리에 'age'라는 키가 있다고 가정

students.sort(key=lambda x:x['age'])
```

`.reverse()`: 리스트를 반대로 뒤집는다. (정렬 X)
- 원본의 순서를 뒤집고 수정하는 것
- 내장 함수 `reversed()`는 원본을 변형시키지 않지만 `.reverse()`는 원본을 변형시킨다.



### 3. 튜플
- 변경 불가능
- 값을 변경하는 메서드 사용 불가

#### 탐색
`.index(x, srart, end)`: 첫번째로 나오는 x의 index 값 출력
- start, end 값에 index를 넣으면 그 range 안에서 x 탐색하여 index 반환
- x의 값이 튜플에 없으면 오류 생김

`.count(x)`: 튜플에서 x가 등장하는 횟수 반환


## 순서가 없는 데이터 구조
### 셋
- 변경 가능
- 순서 없음
- 순회 가능함
#### 변경
`.add(x)`: x값을 set에 추가한다.
- set은 중복을 허용하지 않기 때문에 같은 x의 값으로 여러번 add를 실행해도 결과적으로 set에는 하나의 x만 추가됨

`.update(*others)`: 여러값을 추가한다. (순회가능한 값을 추가해야 한다.)
```
a = {'a', 'b'}

a.update({'c', 'd'}, {'e'})
# {'a', 'b', 'c', 'd', 'e'}
```

`.remove(x)`: x을 set에서 삭제
- x가 set에 없을 시 오류

`.discard(x)`: x를 set에서 삭제
- x가 set에 없어도 오류 X

`dir(set)`: set에 사용되는 메서드 확인

### 딕셔너리
- 변경 가능
- 순서 X
- 순회 가능
- key: value

#### 조회
`.get(key, default)`: key를 통해 value를 가져옴
- key가 딕셔너리 내에 없을 경우 오류 발생하지 않음
- `my_dict[key이름]`에서는 key이름을 가진 key가 없을 경우 오류를 발생함
- `defalut` 값은 key가 없을 때 오류를 반환하는 대신 default 값을 반환하도록 되어 있다.


`.setdefault(key, default)`: key를 통해 value를 가져오고 key가 딕셔너리에 없을 경우 default 값을 value로 가지는 key를 딕셔너리에 삽입하고 default를 반환한다.
```
my_dict = {'apple': '사과'}

my_dict.setdefault('pineapple', '파인애플')
# '파인애플' 반환

my_dict
# {'apple': '사과', 'pineapple', '파인애플'}
```

#### 변경
`.pop(key, default)`: key에 해당하는 key:value를 삭제하고 그 value 반환
- key가 없으면 default값을 반환한다.
- default 값이 설정되어 있지 않으면 오류를 발생시킨다.

`.update(x)`: 다른 딕셔너리나 key/value 쌍으로되어 있는 순회 가능한 자료형 x로 update
- key가 이미 있는 key라면 value의 값을 x에 있는 value의 값으로 update
- 없는 key:value라면 새로 추가
```
my_dict = {'apple': '사과'}

my_dict.update({'apple':'사과아'})
# my_dict의 '사과'가 '사과아'로 바뀜

my_dict.update({'banana': '바나나'})
# 새로 추가됨
```

`dir(dict)`: 딕셔너리에서 사용할 수 있는 모든 메서드 반환


## 얕은 복사와 깊은 복사

### 1. 할당
- 두 개 중 하나만 변경되어도 수정되는 현상이 동일하게 발생
```
original = [1, 2, 3]

copy = original
# copy와 original은 같은 주소값을 가지게 된다.

copy[0] = 5

original  # [5, 2, 3]

id(copy) == id(original)  # True
```

### 2. 얕은 복사
- 일부에서 서로 다르게 복사 가능
- 2차원 list와 같은 경우 mutable객체 안의 mutable객체의 주소값이 같은 경우가 발생해 얕은 복사는 한정적인 복사이다.

#### 1. slice 연산자 [:]
- 슬라이싱하여 할당 시 새로운 id가 부여되어 두개가 서로 영향을 받지 않는다.
- `b = a[:]` 으로 a와 주소값이 다르고 새로운 b 생성

#### 2. list()
```
a = [1, 2, 3]

b = list(a)  # 다른 주소값
```

#### 3. copy()
```
a = [1, 2, 3]

b = a.copy()   # 다른 주소값
```

### 깊은 복사
- 새로운 객체를 만들고 원복 객체 내에 있는 객체에 대한 복사를 **재귀적**으로 삽입한다.
- 따라서 2차원 list와 같은 객체에 대해 내부에 있는 모든 객체까지 새롭게 값이 변경됨
- `copy.deepcopy(a)`를 사용하여 a에 대한 깊은 복사를 진행한다. (내장 모듈)
- 