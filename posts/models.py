from django.db import models

# Create your models here.
#column을 설정하는 것 -> modeling 을 한다(어떤 데이터를 넣을지 설정)
# 앱의 이름은 복수형, class 의 이름은 단수형으로 
class Post(models.Model): # models 모듈에서 Model 이라는 class를 상속
    title = models.CharField(max_length=100)
    conten = models.TextField()