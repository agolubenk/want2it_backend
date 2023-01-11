from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacancy
from blog.models import Blog
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def vacancy_list(request):
    """Формирует список статей"""
    vacancys = Vacancy.objects.filter(activity=1).order_by('-vacancy_date')
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    return render(request, 'vacancy/list.html', {'vacancys': vacancys, 'menuposts':menuposts})



def vacancy_detail(request, pk):
    """Формирует отдельную статью и список"""
    vacancy = get_object_or_404(Vacancy, pk=pk)
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    return render(request, 'vacancy/detail.html', {'vacancy': vacancy, 'menuposts':menuposts})

