# 기초 문법
1. 들여쓰기 (Indentation)
   
   들여쓰기 = space키 4칸이나 Tab키 1번
   ```
   #space키 4번(1탭) 사용해야 할 때
   if True:
        print(True)
    else:
        print(False)

    #space키 1번 사용해야 할 때
    a = 'apple'
   ```
   - 하나의 코드 안에서는 반드시 한 종류의 들여쓰기 사용
   - PEP8 형식에 따라 공백 사용

2. 변수 (Variable)
   1. 변수
   
    이름(변수)에 값(객체)을 저장(할당)한다.

    값(객체) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것 의미/ 파이썬은 모든 것이 값(객체)로 구현됨

    ```
    x = 1   # 이름(변수) = 값(객체)
    # 이름에 다른 값을 언제든지 할당할 수 있음
    # x에 1을 저장한다라고 표현

    i = i - j
    # 순서는 이름에 값을 저장하는 것이기 때문에 i-j가 먼저 계산되고 i에 적용되는 것이다
    ```

   2. 할당 연산자 (Assignment Operator)
   
   - `=` : 변수에 값 할당할 때
   - `type()` : 데이터 타입 확인
   - `id` : 값의 메모리 주소 확인
   ```
   name = '정혜원'
   type(name)
   id(name)
   ```
   3. 변수 할당
   - 같은 값 동시 할당
  
   ```
   x = y = 100
   ```

   - 다른 값 동시 할당
   ```
   x, y = 1, 2
   ```

   - 임시변수를 사용하지 않고 x와 y의 값을 바꾸는 방법
   ```
   # 임시변수 사용
   a = x
   x = y
   y = a

   # pythoninc
   y, x = x, y

   # 다른 방법
   x = x + y
   y = x - y
   x = x - y
   ```
   4. 식별자 (Identifiers)
   
   *식별자 이름의 특징*
   - 영문 대소문자, 언더스코어(_), 숫자로 구성
   - 첫 글자에 숫자 X
   - 길이 제한 X
   - 대, 소문자 구별 O 
   - True와 False와 같은 키워드 사용 X (실행 자체가 안됨)
     - ```
        import keyword
        print(keyword.kwlist)
       ```
       위 코드 입력시 출력되는 키워드들 사용 X
    - 내장함수나 모듈 등의 이름 사용 X
      - ```
        print = 'hi'      # 실행됨
        print(100)      # 오류 생김

        del print       # 위에 print에 잘못 할당된 값 삭제
        print('good')     # 정상적으로 작동됨

        dir(__builtins__)    # print()처럼 변수화하면 안되는 함수, 모델들 반환
        ```
      - 다른 값이 할당되면 내장함수나 모듈 동작 X
      - 실행은 되나 내장함수나 모듈의 원활한 이용을 위해 사용 X

   5. 사용자 입력 (Input)
   
   - 파이썬 내장 함수
   - 사용자 입력값 받을 수 있음
   - **input 반환값은 항상 문자열(str)의 형태로 반환된다**
   ```
   data = input()
   print(data)
   # data에 정수인 100값을 input해도 print(data) 값은 '100'으로 str 문자열 형태로 출력됨

   name = input('이름을 입력 해 주세요 : ')
   print(name)
   ```
   6. 주석
   
   - `#` : 한 줄 주석
   - `'''` 또는 `"""` : 여러 줄 주석
   - ctrl + / : 여러 줄을 드래그 한 후 ctrl + / 누르면 각 줄이 `#`으로 주석 처리됨
   ```
   # 한 줄 주석 연습
   ```




# 자료형 (Data Type)
1. 자료형 분류

- 밑에 2~5까지의 목차가 자료형 분류이다.

2. Boolean Type (불린형)
   
- `bool` type : `True`와 `False`
- 비교/논리 연산 수행
  ```
  type(True)   # bool
  type(False)   # bool

  bool(0)   # false
  bool('')   # false
  bool([])   # false
  # 비어있다라는 개념이면 false 반환

  bool(1)   # true
  bool(-1)   # true
  bool([1,2,3])   # true
  # 비어있지 않으면 true 반환
  ```
3. Numeric Type (수치형)
   1. int (정수)
   - 8진수, 2진수, 16진수로도 표현 가능
   - 파이썬에서 표현할 수 있는 가장 큰 정수
     - ```
       import sys
       max_int = sys.maxsize
       print(max_int)

       super_max = sys.maxsize * sys.maxsize
       print(super_max)
       ```
     - sys 모듈을 불러서 가장 큰 숫자 활용
     - 파이썬은 임의 정밀도 산술을 사용하기 때문에 오버플로우 X
     - **오버플로우** : 메모리의 크기가 제한되어 있어 표현할 수 있는 수의 범위를 넘어가는 연산을 할 시 출력되지 않는 상황
     - **임의 정밀도 산술** : 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태로 이로 인해 오버플로우가 발생하지 않음
     - 따라서 파이썬이 사용 가능한 숫자는 메모리가 남아 있는데까지 사용 가능하다.
   2. float (부동소수점/실수)
   - 실수를 표현하는 과정에서 부동소수점이 항상 같은 값으로 일치 X
   - **지수 표현 방식** : e 사용
   - ```
     5e3   # 5000
     314e-2   #3.14
     # 소수점 위치 결정
     ```
   - 실수의 연산 : 실제 값이 안나올 수 있음
     - ```
       3.5 - 3.12 == 0.38  # false

       x = 3.5 - 3.12
       # 반올림
       round(x, 2)  # 소수점 둘째자리까지 반올림
       # 올림
       import math
       math.ceil(x)
       # 내림
       math.floor(x)
       ```
     - 3.5 - 3.12와 0.38은 실질적으로 같으므로 이를 처리하기 위한 방법 3가지가 있다
       - ```
         a = 3.5 - 3.12
         b = 0.38
         
         # (1) a와 b의 차이가 1e-10 이하면 두 값이 같다고 볼 수 있음
         abs(a - b) < 1e-10 

         # (2) a와 b의 차이가 sys.float_info.epsilon 이하면 같다고 볼 수 있음
         import sys
         abs(a - b) <= sys.float_info.epsilon

         # (3) math.isclose()
         import math
         math.isclose(a, b)
         ```
   3. complex (복소수)
   - 실수부와 허수부로 구성
   - complex number의 허수부는 `j`로 표현
   - ```
     (0 + 2j) ** 2  #(-4+0j)
     ```
4. String Type (문자열)
   1. 문자열 (Str)
   - single quotes(')나 double quotes(")로 표현
   - single이나 double 중 하나의 문장부호 선택해서 유지 사용하면 됨 (PEP-8 조건)
   - ```
     s = 'hello'
     # 철수 '안녕'
     print('철수 \'안녕\'') 
     # 철수 "안녕"
     print('철수 \"안녕\"')

     # hi 정혜원 출력
     print('hi', '정혜원')
     ```
    - **중첩 따옴표**(Nested Quotes) : 따옴표 안에 따옴표 표현
      - ```
        '작은 "큰"'  # 가능
        "'작은' 큰"  # 가능
        ```
    - **삼중 따옴표**(Triple Quotes) : 따옴표들을 삼중으로 사용
      - 문자열 안에 따옴표 넣을 때
      - `'''` : 여러 줄에 걸쳐있는 문장 표현할 때
      - ```
        print('''
        문자열 안에 '작은 따옴표'나
        "큰 따옴표"를 사용할 수 있고
        여러 줄을 사용할 때도 편리하다.
        ''')
        ```

   2. 이스케이프 시퀀스 (Escape Sequence)
   - `\` : 문자열에서 특수문자나 조작을 위하여 사용됨
   - |예약문자|내용(의미)|
     |---|---|
     |\n|줄 바꿈|
     |\t|탭|
     |\r|캐리지리턴|
     |\0|Null|
     |`\`|`\`|
     |\'|단일인용부호(')|
     |\"|이중인용부호(")|
     ```
     len('\'')  #1  (예약문자들은 한 글자로 인식)

     print('이 다음은 에터. \n그리고 탭\t탭')
     #
     ```

   3. String Interpolation
   - %-formatting
     - %d : 정수
     - %f : 실수
     - %s : 문자열
    ```
    name = '정혜원'
    score = 3.5

    print('내 이름은 %s, 성적은 %f' % (name, score))
    ```
   - str.format()
    ```
    print('내 이름은 {}, 성적은 {}' .format(name, score))
    ```
   - **f-strings**
    ```
    print(f'내 이름은 {name}, 성적은 {score}')

    # 여러줄 문자열에서도 가능
    print(f'''안녕하세요
    제 이름은
    {name}입니다.''')

    # f-strings에서는 형식 지정 가능

    import datetime
    today = datetime.datetime.now()
    print(today)

    print(f'오늘은 {today:%Y}년')

    # f-strings에서는 연산과 출력형식 지정도 가능

    pi = 3.141592
    print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi * 2 * 2}이라고 출력해봅시다.')  
    # 소수점 3번째 자리에서 반올림
    ```
        - 여러 줄 문자열에서 가능
        - 형식 지정 가능
        - 연산과 출력형식 지정 가능
5. None Type
- 값이 없음을 표현하기 위한 타입임
```
type(None)   #NoneType

a = None
print(a)
#None
```



