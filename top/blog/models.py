from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='image.jpg', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:20] + '...читать далее'
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name

