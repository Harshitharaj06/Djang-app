from django.db import models

# Create your models here.
class Post(models.Model):
    picture=models.ImageField(default="default.png")

