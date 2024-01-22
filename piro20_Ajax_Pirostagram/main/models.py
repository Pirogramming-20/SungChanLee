from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')