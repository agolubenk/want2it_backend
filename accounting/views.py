from django.shortcuts import render, redirect, get_object_or_404
from .models import Price, Tarif
from blog.models import Blog
from contacts.models import Contact
from vacancy.models import Vacancy
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def price(request):
    """Формирует список статей"""
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    prices = Price.objects.filter(activity=1)
    vacancys = Vacancy.objects.filter(activity=1).order_by('-vacancy_date')
    contacts = Contact.objects.filter(title='Организация')
    tarifs = Tarif.objects.filter(activity='Активный')
    return render(request, 'price.html', {'menuposts': menuposts, 'prices': prices, 'tarifs': tarifs, 'vacancys': vacancys, 'contacts': contacts})
