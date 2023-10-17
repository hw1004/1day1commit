from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.pk}) {self.name}'
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name='movies')
    
    def __str__(self):
        return f'{self.pk} => {self.title}'
    
# class ActorMovie(models.Model):
#     actor = models.ForeignKey(Actor)
#     movie = models.ForeignKey(Movie)
    
if __name__ == '__main__':
    m1 = Movie.objects.get(pk=1)
    m2 = Movie.objects.get(pk=2)
    m3 = Movie.objects.get(pk=3)
    m4 = Movie.objects.get(pk=4)
    m5 = Movie.objects.get(pk=5)
    
    a1 = Actor.objects.get(pk=1)
    a2 = Actor.objects.get(pk=2)
    a3 = Actor.objects.get(pk=3)
    a4 = Actor.objects.get(pk=4)
    a5 = Actor.objects.get(pk=5)
    # M:N 관계 추가
    # 영화에 배우 추가
    m1.actors.add(a4)
    m3.actors.add(a2)
    
    # 배우에 영화 추가(related_name 때문에 movies)
    a4.movies.add(m1)
    a2.movies.add(m3)
    
    # M:N 조회 코드
    a2.movies.all()
    m1.actors.all()
    
    # M:N 삭제 코드 (아래 두개 중 하나 선택)
    a2.movies.remove(m3)
    m3.actors.remove(a2)
    
    # m3의 출연진 중 첫번째 출연진의 필모
    
    