from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,"home.html",{'items': posts})

    
