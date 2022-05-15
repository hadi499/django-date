from django.shortcuts import render
from datetime import datetime
from .models import Post


def home(request):
    today = datetime.today()
    posts = Post.objects.filter(date=today)
    return render(request, 'blog/index.html', {'posts': posts})
