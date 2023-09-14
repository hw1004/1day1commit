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
    def instance_method(self):
        return self
    
    @classmethod
    def class_method(cls):
        return cls
    
    @staticmethod
    def static_method():
        return 100
```
- 그냥 함수처럼 작용하기 때문에 인스턴스와 클래스의 속성과 무관

## 인스턴스와 클래스 간의 이름 공간
- 인스턴스에서 속성에 접근하면 인스턴스, 클래스 순으로 탐색
- 클래스 정의하면 클래스와 해당하는 이름 공간 생성됨
```
class Person:
    # class 변수
    spices = 'human'

    # instance 메서드
    def __init__(self, name):
        # instance 변수
        self.name = name

p1 = Person('Jung')
```
- 인스턴스 변수가 인스턴스 메서드에 지정된 적이 없으면 클래스 변수를 탐색한다.
```
class Person:
    name = 'unknown'

    def talk(self):
        return self.name

p1 = Person()
p1.talk()    # unknown

p2 = Person()
p2.name = 'Jung'
p2.talk()     # Jung

p2.name, Person.name  # ('Jung', 'unknown') Person 클래스의 값이 변경된 것은 아님
```

**LEGB** : Local - Enclosed - Global - Builtin 순서대로 출력한다.
```
a = 100
class Sample:
    a = 1

    def func(self):
        b = 2
        return a + b   # 102
        return self.a + b  # 3

s = Sample()
s.func()
# sample 변수를 인스턴스 메서드에 사용하고 싶으면 self를 붙여야 사용 가능함.
```

## 인스턴스, 클래스, 메서드
- **인스턴스**는 인스턴스 메서드, 클래스 메서드, 정적 메서드에 모두 접근할 수 있음
  - 인스턴스 메서드만 인스턴스가 할 행동을 모두 포함한다.
- **클래스**는 인스턴스 메서드, 클래스 메서드, 정적 메서드에 모두 접근할 수 있음
- 클래스 메서드 : 클래스 자체와 그 속성에 접근해야 할 때
- 정적 메서드 : 클래스 자체와 그 속성에 접근할 필요가 없을 때 (정적 메서드는 묵시적인 첫번째 인자(cls, self)를 받지 않음)
- *인스턴스 메서드는 인스턴스로부터 호출되어야 하며 클래스로부터 호출 될 수 없다.*


## OOP의 핵심 개념
1. 추상화(Abstraction)
   - 필수적인 부분만 표현하는 것
   - 여러 클래스가 공통적으로 사용하는 속성 및 메서드를 추출해서 기본 클래스로 작성
   - (ex) Student와 Teacher의 공통된 속성 및 메서드를 이용하여 Person class를 새로 작성
2. 상속(Inheritance)
   - 부모 클래스의 모든 속성이 자식 클래스에게 상속
   - 코드의 재사용성이 높아짐
   - (ex) `class Student(Person)`처럼 새로운 클래스를 만들 때 기존의 클래스를 상속받게 하면 Student 클래스에 없는 속성도 Person으로부터 상속받아 사용 가능
   - Student의 인스턴스가 Person에 없는 속성을 활용하고 싶을 때는 Person을 상속받을 때 `__init__` 함수에 새로운 속성을 넣으면 됨
   - `issubclass(Student, Person)` : Student class가 Person class의 subclass인지 확인할 때 (상속받은 관계, 인스턴스-클래스 관계, bool-int 관계 등 확인할 때) 
   - `super()` : 자식 클래스에 메서드 추가로 구현 가능
   - ```
     # Person class에 있는 
     self.name = name
     self.age = age
     self.number = number
     self.email = email

     # 이 인스턴스 변수들을 Person class를 상속받은 Student class에서도 똑같이 적용할 때
     super().__init__(name, age, number, email)
     self.student_id = student_id
     # 위에처럼 새로 추가되는 인스턴스 변수만 정의해주고 나머지 상속받은 속성들은 super()을 사용하여 표현해준다.
     ```
3. 다형성(Polymorphism)
   - 동일한 메서드가 class에 따라 다르게 행동할 수 있음
   - **메서드 오버라이딩**
     - 자식 클래스에서 부모 클래스이 메서드 재정의
     - (ex) Animal class와 Person class에서 동일하게 talk() 메서드가 있다고 하자. Person class는 Animal class를 상속받았을 때, 다형성을 이용하여 Animal 인스턴스는 Animal class의 talk()에 해당하는 결과값을, Person 인스턴스는 Person class의 talk()에 해당하는 결과값을 내놓는다. 이는 Animal class의 talk() 메서드를 Person class의 talk()로 덮어씌운 것이다.
4. 캡슐화(Encapsulation)
   - 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스를 차단하는 것(암묵적으로 존재)
   1. Public member
      - 언더바 없는 메서드나 속성들
      - 어디서나 호출 가능
   2. Protected member
      - 언더바 하나(_)로 시작하는 메서드나 속성들
      - 암묵적으로 부모 클래스 내부와 자식 클랫스에서만 호출 가능
      - 밖에서 호출하면 안됨(출력은 되지만 하지 않음)
      - (ex) `self._age = age`
   3. Private member
      - 언더바 두개(__)로 시작하는 메서드나 속서들
      - 본 클래스 내부에서만 사용 가능!
      - (ex) `__init__(self, name)`
      - (ex) `self.__age`
      - Protected는 접근은 가능하지만 private은 직접 접근이 불가능하다!
      - (ex) `return self.__age`를 출력하는 함수를 호출하여 간접적으로 접근할 수 있다.
   4. 다중 상속
      - 두개 이상의 클래스 상속받는 경우
      - 중복된 속성 또는 메서드가 있는 경우 상속 순서에 따라 결정함
      - (ex) class Person, class Mom(Person), class Dad(Person), class FirstChild(Dad, Mom), class SecondChild(Mom, Dad) 처럼 Mom과 Dad 두 클래스를 모두 상속받는 경우
      - Firstchild class에 없어도 Dad 또는 Mom 클래스에 있는 메서드나 속성인 경우 Firstchild 인스턴스에서도 호출 가능
      -  Mom과 Dad class에 gene이라는 속성이 공통적으로 있고, Mom class는 `gene = 'XX'`, Dad class는 `gene = 'XY'` 일 때 상속 순서에 따라 Firstchild는 XY, SecondChild는 XX를 호출받는다.
    5. 상속관계에서의 이름 공간과 MRO
       - MRO(Method Resolution Order) : 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 속성 또는 메서드
       - 상속 관계 탐색 순서 : 인스턴스 -> 자식 클래스 -> 부모 클래스
       - ```
         print(FirstChild.__mro__)

         # (<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>)
         ```


