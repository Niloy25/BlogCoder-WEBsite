from blogCoder.settings import USE_TZ
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    thumbnail = models.ImageField(upload_to="post/images", default="")
    timeStamp = models.DateTimeField(default=now, blank=True)

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)