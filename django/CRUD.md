# CRUD
- CREATE 생성
- READ 조회
- UPDATE 수정
- DELETE 삭제


## 1. CREATE
students app 내의 models.py에서 Student class가 있을 때...

1. 인스턴스 생성
   1. `s = Student()`로 Student class의 인스턴트 s를 지정해준다.
   2. `s.name`, `s.major` 등 Student Class 내의 칼럼들의 값을 지정해준다.
   3. `s.save()`를 이용하여 생성한 인스턴스의 값들을 저장해준다.
2. `Student.objects.create`
   1. `Student.objects.create()`를 작성한다.(Student는 class명이다.)
   2. `name, major, age` 등의 칼럼들의 값을 지정해준다.


## 2. READ
### 전체 조회
`Student.objects.all()`을 이용하여 table 전체 조회
### 단일 조회
`Student.objects.get(name='정혜원)`과 같이 특정 칼럼명을 가진 인스턴스를 조회할 수 있다. name 뿐만 아니라 id, age 등의 다른 값들로도 조회 가능하다.

## 3. UPDATE
```
s1 = Student.objects.get(pk=1)
s1.age = 21
s1.save()
```
단일 조회로 수정하고자 하는 인스턴스를 지정하고 인스턴스 내에서 바꾸고자 하는 칼럼을 지정해 원하는 값으로 재지정한다. 그 후 `.save()`를 적용하면 값이 수정된다.

## 4. DELETE
위와 같이 `s2 = Student.objects.get(pk=2)`처럼 삭제하고자 하는 인스턴스를 지정 후 `s2.delete()`를 이용해 삭제한다.