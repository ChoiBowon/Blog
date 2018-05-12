from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) #회원이 사라지면 관련된 데이터도 지워 달라는 것
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='Blog/thumbnail/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title