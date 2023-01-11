from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def blog_list(request):
    """Формирует список статей"""
    posts = Blog.objects.filter(draft=1).order_by('-blog_date')
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    return render(request, 'blog/list.html', {'posts': posts, 'menuposts': menuposts})



def blog_detail(request, pk):
    """Формирует отдельную статью и список"""
    post = get_object_or_404(Blog, pk=pk)
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    return render(request, 'blog/detail.html', {'post': post, 'menuposts': menuposts})

