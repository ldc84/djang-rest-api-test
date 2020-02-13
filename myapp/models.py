from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  text = models.TextField()
  image = models.ImageField(upload_to="%Y/%m")

class Comment(models.Model):
  text = models.CharField(max_length=200)
  post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, blank=True)