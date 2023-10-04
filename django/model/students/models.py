from django.db import models

# 테이블 명
# 컬럼 명 = 데이터 타입

class Student(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField(default='')
    major = models.CharField(max_length=100)
    age = models.IntegerField()
    cgpa = models.FloatField()
    # is_graduated = models.BooleanField(default=False)   # non-nullable field errror solution

if __name__ == '__main__':
    pass
    # CRUD
    
    # Create 생성
    s = Student()
    s.name = '정혜원'
    s.major = '응용수학통계학'
    s.age = 20
    s.address = '용인'
    s.cgpa = 3.7
    s.save()
    
    Student.objects.create(
        name = '김땡땡',
        major = '경영',
        age = 22,
        address = '부산',
        cgpa = 3.3,
    )     # 삭제된 인스턴스의 id를 사용하지 않는다.(2가 삭제되면 새 인스턴스 생성 시 3을 쓴다.)
    
    # Read 조회
    # 1. 전체 조회
    students = Student.objects.all()
    for student in students:
        print(student.name, student.major)
    # 2. 단일 조회
    Student.objects.get(name='정혜원')   # 중복되는 데이터가 있으면 처음 발견한 하나만 가져옴
    s1 = Student.objects.get(id=1) # id는 중복되지 않기 때문에 사용하기 좋음(pk라고 써도 됨)
    print(s1.pk, s1.name, s1.address, s1.cgpa)
    
    # Update 수정
    s1 = Student.objects.get(pk=1)
    s1.age = 21
    s1.save()
    
    # Delete 삭제
    s2 = Student.objects.get(pk=2)
    s2.delete()
    
