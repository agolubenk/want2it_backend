from django.shortcuts import render, redirect, get_object_or_404
from .models import Price, Tarif
from blog.models import Blog
from contacts.models import Contact
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def price(request):
    """Формирует список статей"""
    vacancys = Price.objects.filter(activity=1).order_by('-vacancy_date')
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    contacts = Contact.objects.filter(title='Организация')
    return render(request, 'vacancy/list.html', {'vacancys': vacancys, 'menuposts':menuposts, 'contacts': contacts})

