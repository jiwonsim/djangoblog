from django.db import models
from django.utils import timezone

class Post(models.Model): # Post라는 장고 모델 정의 
    #속성 정의
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank = True, null = True)
        
    #publish 메서드 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #아래 함수를 호출한다면 Post모델의 제목을 얻게 된다.
    def __str__(self):
        return self.title