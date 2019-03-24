from django.conf import settings
from django.db import models
import random

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumb = models.ImageField(upload_to="thumbnail")
