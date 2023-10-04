from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=100)
    room = models.TextField()
    year = models.IntegerField()
    
    
# 실습
# id, name, major, room, year을 가진 4명
# from professors.models import Professor

if __name__ == '__main__':
    # Create
    Professor.objects.create(
        name='kim',
        major='CSE',
        room='k101',
        year=5,
    )
    Professor.objects.create(
        name='park',
        major='MAN',
        room='e554',
        year=10,
    )
    Professor.objects.create(
        name='lee',
        major='KOR',
        room='d331',
        year=4,
    )
    Professor.objects.create(
        name='choi',
        major='CSE',
        room='p224',
        year=2,
    )
    
    # Read
    # 전체 조회
    professors = Professor.objects.all()
    for professor in professors:
        print(professor.name, professor.major, professor.room, professor.year)
    # 단일 조회
    s1 = Professor.objects.get(name='kim')
    print(s1.name, s1.major, s1.room, s1.year)
    
    # Update
    sc = Professor.objects.get(name='choi')
    sc.year = 3
    sc.save()
    
    sk = Professor.objects.get(name='kim')
    sk.room = 'k102'
    sk.save()
    
    # Delete
    sl = Professor.objects.get(name='lee')
    sl.delete()
    
    sp = Professor.objects.get(name='park')
    sp.delete()