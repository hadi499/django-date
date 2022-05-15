from turtle import title
from django.db import models
from django.forms import CharField


class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
