from django.shortcuts import render
from .models import Post
# Create your views here.

posts = [
    {
        'author' : 'Sagar',
        'title' : 'Post1',
        'content' : 'First content by Python',
        'date_posted' : '27 May, 2021'
    },
     {
        'author' : 'Deep',
        'title' : 'Post2',
        'content' : 'Second content by Python',
        'date_posted' : '27 May, 2021'
    }
]


def home(request): #To return what users will see
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

