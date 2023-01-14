from django.shortcuts import render, redirect, get_object_or_404
from vacancy.models import Vacancy
from blog.models import Blog
from contacts.models import Contact
from .models import Order
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def order(request):
    """Формирует список статей"""
    vacancys = Vacancy.objects.filter(activity=1).order_by('-vacancy_date')
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    contacts = Contact.objects.filter(title='Организация')
    return render(request, 'form.html', {'vacancys': vacancys, 'menuposts':menuposts, 'contacts': contacts})



