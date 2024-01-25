from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_description = models.TextField()
    post_catrgory = models.CharField(max_length=20)