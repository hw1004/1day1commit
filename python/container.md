# 컨테이너 (Container)
컨테이너 : 여러 개의 서로 다른 값 저장 가능

1. 컨테이너 분류
   - 시퀀스형 : 순서 O
     - list, tuple, range, string, binary
   - 비시퀀스형 : 순서 X
     - set, dict

2. 시퀀스형 컨테이너
   - 데이터가 순서대로 나열된 형식
   - 나열 O, 정렬 X
   - 특정 위치의 데이터 가리킬 수 있음 (인덱스)


    1. 리스트
    - [], list()
    - list의 요소가 여러개 일 때 변수 이름 복수형으로
    - `list[i]` : 값에 대한 접근
    - 가변형
    - `len(boxes)` : 리스트의 길이 산출(요소의 개수)
    - index

     ```
     boxes = ['a', 'b', 'c']

     boxes[2]    # c
     boxes[-1]   # c
     ```
    
    2. 튜플
    - ()
    - 불변
    - `()` : 빈 튜플은 type 출력시 튜플로 표시된다
    - 튜플은 데이터 추가/수정/삭제 모두 불가능(immutable)
    - 주의 사항

      ```
      # 단일 항목의 튜플인 경우 쉼표를 붙여야 함
      a = (1, )
      print(type(a))   # tuple

      b = (1)
      print(type(b))    # int

      # 복수 항목의 튜플인 경우 마지막 항목의 쉼표는 생략 가능
      multi_tuple = (1, 2, 3,)
      multi_tuple = (1, 2, 3)
      # 둘 다 가능
      ```
    - 튜플 대입 (우변 -> 좌변 변수 할당)
      ```
      x, y = 1, 2    #무조건 튜플로 처리
      (x, y) = (1, 2)
      ```
    
    
    3. 레인지
    - **정수**의 시퀀스
    - `range(n)` : 0부터 n-1까지의 값
    - `range(n, m)` : n부터 m-1까지의 값
    - `range(n, m ,s)` : n부터 m-1까지 s만큼 증가
    - a <= x < b

    - ```
      # range 내의 모든 정수값 나열하고 싶을 때
      list(range(0,10))
      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

      # 특정 값이 range 안에 있는지 확인하고 싶을 때
      2 in range(1, 4)  # T
      2.1 in range(1,4)  # F (range는 정수만 다루고 실수는 다루지 않음)
      ```
    - range는 수정 불가능
   

      ### 패킹/언패킹 연산자
      - 모든 *시퀀스형* (*list, tuple, range, string*)은 패킹, 언패킹 가능
      #### 패킹
      - 변수에 사용됨 (*)
      - 우변 객체 수 > 좌변 객체수 : 객체 순서대로 대입
      - 나머지 항목들은 *변수에 **list**로 대입됨
      - ```
        x, *y = 1, 2, 3
        print(x, y)
        # 1,[2, 3]
        ```
      #### 언패킹
      - 튜플 형태로 대입 (*argument)

      - ```
        def multiply(x, y, z):
            return x * y * z
        
        num = [1, 2, 3]
        multiply(*num)  # multiply(1, 2, 3) 형태로 대입됨
        ```
      
       - 곱셈 기호와 패킹/언패킹 연산자를 잘 구분할 것!

3. 비 시퀀스형 컨테이너
    1. 세트 
    - {}
    - 순서가 없고 중복된 값이 없음
    - 집합과 동일 개념
    - 가변형
    - `set()` : 빈 세트 생성
    - {}로 빈 세트를 만드는 것은 불가능하다 (빈 dict을 만드는 데 사용)
    - 차집합, 합집합, 교집한 연산자 사용 가능 (`-, |, &`)
    - ```
      s1 = {1, 1, 3, 3, 3}
      s1
      # {1,3} 중복된 값 제거

      # list의 중복된 값 제거할 때 set 사용
      alphabets = ['a', 'a', 'b', 'b']

      set(alphabets)  # {'a', 'b'}
      list(set(alphabets))  #['a', 'b']
      ```
    - 수정 가능 (할당 방식이 아닌 매서드로 변경) - 순서 없기 때문에 인덱스 지정 없음
      ```
      s = {1, 2, 3}

      s.add(4)   # 4 추가

      s.remove(2)  # 2 삭제
      ```
    
    2. 딕셔너리
    - key와 value로 이루어져 있음
    - {}, dict()
    - 순서 보장하지 않음
    - key: 변경 불가능 데이터만 (string, integer, float, bool, tuple, range)
    - value: 모든 데이터 올 수 있음
    - key는 중복될 수 X, value는 중복될 수 O
    - ```
      phone_book = {'서울': '02', '경기': '031', '인천': '032', '대전': '042', '광주': '062'}

      phone_book.keys()  # key만

      phone_book.values()  # value만

      phone_book.items()  # key와 value 세트로만
      ```
    
    - 수정 가능
      - `phone_book['평양'] = '냉면'` : Key-Value 추가 가능
      - `phone_book['서울'] = '022'` : Value 수정 가능
    - 표 데이터 출력 예시
      ```
      table = [
      {'이름': '김김김', '나이': 25, 'MBTI': 'ENTJ'},
      {'이름': '이이이', '나이': 28, 'MBTI': 'INTP'},
      {'이름': '박박박', '나이': 21, 'MBTI': 'ESFJ'},
      ]
      ```

4. 형 변환 (Type conversion)
   - 암시적 형 변환: 자동
     - ex: `print(True + 3)` 4 출력
   - 명시적 형 변환: 의도
     - ex: `print(int('3'))`

![컨테이너형 형 변환]("https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png")

     - 컨테이너형들은 range와 dictionary로는 형 변환이 안된다.
     -  dictionary는 string을 제외하고 나머지 형태로 형 변환을 할 때 key만 나열되는 형식으로 형 변환이 일어난다. 


5. 컨테이너
   컨테이너
   - 시퀀스형
     - list (immutable)
     - string (mutable)
     - tuple (mutable)
     - range (mutable)
   - 비시퀀스형
     - set (mutable)
     - dictionary (mutable)

6. 시퀀스형 연산자
   - 시퀀스를 연결 가능
   - 산술 연산자(+)
     - list, tuple, string 가능
     - range 불가능
   - 반복 연산자(*)
     - list, tuple, string 가능
     - range 불가능
   - 인덱싱
     - 접근 []
     - 시퀀스의 특정 인덱스 값에 접근
     - 오류: 인덱스가 범위 내에 없을 때 (IndexError)
   - 슬라이싱
     - [:] 슬라이싱
     - [n:m] : n이상 m-1 이하
     - [:m] : m-1 이하
     - [n:] : n 이상
     - [n:m:s] : n부터 s씩 건너서 m-1 이하 값까지
     - range(p)[n:m] : range(n,m)과 같음
     - [::] : 원래값 그대로
     - [::-1] : 원래값 거꾸로




7. 함수, 모듈, 패키지, 라이브러리
- 함수: 특정 명령 수행하는 함수 묶음
- 모듈: 함수/클래스의 모음, 하나의 프로그램을 구성하는 단위
- 패키지: 프로그램 + 모듈
  - 프로그램: 실행하기 위한 것
  - 모듈: 다른 프로그램에서 불러와서 사용하기 위한 것
- 라이브러리: 패키지의 모음
- 요약: 함수 + 클래스 => 모듈 => 모듈 + 프로그램 => 패키지 => 라이브러리




8. 정리
- 변수명(식별자)
- 데이터(값)
- 연산자(operator)
- 데이터 타입
- 형변환(typecasting)
- 표현식(expression)
- 문장(statement)

