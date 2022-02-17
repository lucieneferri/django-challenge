from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.forms import UUIDField

class User(AbstractUser):
    id_user = UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=100, unique= True)
    password = models.CharField(max_length=10)
    email= models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.username

class Author(models.Model):
    id_author = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    picture = models.ImageField()

    def __str__(self):
        return self.name

class Article(models.Model):
    id_article = UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.PROTECT)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    firstParagraph = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

