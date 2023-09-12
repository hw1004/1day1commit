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


