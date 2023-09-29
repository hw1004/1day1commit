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
