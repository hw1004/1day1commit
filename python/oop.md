# OOP(Object Oriented Programming)
- 객체가 중심이 되는 프로그래밍
- 객체들의 모임 + 상호작용(메서드)
- 장점: 유연한 **변경** 용이, **활용** 용이, 직관적 **코드** 분석 가능케함
## OOP 기초
< 객체의 특징 >
- 타입
- 속성(상태/데이터)
- 조작법(행위/함수)

< 기본 문법 >
```
# 클래스 정의
class Myclass:
    pass

# 인스턴스 생성
instance = Myclass()

# 속성 접근
instance.name

# 메서드 호출
instance.method()
```

- **클래스**: 공통 속성과 메서드를 가진 객체들의 분류
- **인스턴스**: 특정 클래스의 객체(인스턴스/데이터의 예시)
-`isinstance(p, Person)`: p가 Person(클래스)의 인스턴스인지 확인

## 속성과 메서드
- **속성**: 객체의 상태/데이터
  - (ex) person.name
- **메서드**: 특정 개체가 할 수 있는 행위
  - (ex) person.talk()
  - (ex) list의 .append(), .reverse(), .sort() 등등


## 인스턴스
**인스턴스** : class에 속하는 객체
- 인스턴스 = 클래스()

**인스턴스 변수** : 인스턴스의 속성
- self.변수명로 정의
- 인스턴스.변수명으로 접근

**인스턴스 메서드** : 인스턴스가 사용할 메서드
```
class MyClass:
    def method(self):

# 메서드 호출 시 첫번째 인자로 self 전달됨
```
- 메서드는 함수이기 때문에 self 이외의 추가적인 인자를 받을 수 있음
- self는 무조건 넣어야 함

**self** : 인스턴스 자신
- 인스턴스 메서드 호출 시 첫번째 인자로 자기 자신 전달
```
p1 = MyClass()

p1 is p1.method() # True
```
**생성자(Constructor) 메서드** : 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드 함수
```
class MyClass:
    def __init__(self, name):
        self.name = name

p1 = Person('정혜원')
p1.name
```
- 인스턴스가 생성될 때 인스턴스의 속성 정의할 수 있음

**소멸자(Destructor) 메서드** : 소멸될 때 자동으로 호출되는 메서드
```
class Person:
    def __init__(self):
        print('응애!')
      
    def __del__(self):
        print('으악..ㅜㅜ')

p1 = Person()
del p1
```
- del을 사용하면 del 소멸자가 작동되어 으악..ㅜㅜ이 나온다.
- p1 = Person()을 두번 정의해도 으악..ㅜㅜ이 나온다. (덮어씌어져서 그 전의 정의된 것이 소멸되기 때문)

## 속성
**속성** : 특정 데이터 타입의 객체들이 가지게 될 상태/데이터
- `self.<속성명> = <값>`
- 속성 값을 덮어씌움으로써 변경할 수도 있음

## 매직(스페셜) 메서드
**매직 메서드** : __가 있는 메서드
- `__something__` 형태
### __str__(self)
```
class Person:
    def __str__(self):
        return '내용'
```
- print(p1) 할 때 보여줄 내용 정의
- etc
```
(1).__add__(2)   # 3

[1, 2, 3].__getitem__(1)   # 2

(3).__gt__(2)  # True
```


## 클래스(Class)
**클래스** : 객체들의 분류를 정의할 때 쓰이는 키워드
```
class <클래스이름>:
    <statement>
```
**클래스 변수**
- 클래스의 속성
- 모든 인스턴스가 공유함
- 클래스 선언 내부에서 정의함

```
class Circle:
    pi = 3.14

Circle.pi
```
위에서 Circle.pi는 인스턴스에 속해있는 값이 아닌 class에 속해 있는 값임

**클래스 메서드**
- `@classmethod` 데코레이터를 사용하여 정의
- 메서드 호출 시 첫번째 인자로 class cls가 전달됨

```
class MyClass:
    @classmethod
    def class_method(cls, a1)
```

**스태틱 메서드**
- `@staticmethod` 데코레이터를 사용하여 정의
- 호출시 self, cls 아무것도 전달되지 않음
- 속성 다루지 않고 단지 행동만을 하는 메서드를 정의할 때 사용
```
class MyClass:
    
```