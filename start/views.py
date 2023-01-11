from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog
from vacancy.models import Vacancy
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def menu_list(request):
    """Формирует список статей"""
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    vacancys = Vacancy.objects.filter(activity=1).order_by('-vacancy_date')
    return render(request, 'index.html', {'menuposts': menuposts, 'vacancys': vacancys})
