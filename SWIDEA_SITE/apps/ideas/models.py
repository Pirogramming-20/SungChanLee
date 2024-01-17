from django.db import models

from apps.devtools.models import DevTool


class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content = models.TextField()
    interest = models.IntegerField()
    devtool = models.ForeignKey(DevTool, on_delete = models.CASCADE, verbose_name= '개발툴')

class Like(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)  # YourItemModel을 실제 모델로 교체
