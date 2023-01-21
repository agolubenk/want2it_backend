from django.shortcuts import render, redirect, get_object_or_404
from vacancy.models import Vacancy
from blog.models import Blog
from contacts.models import Contact
from .models import Order
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic.base import View
from .forms import OrderForms


def upload(request):
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    vacancys = Vacancy.objects.filter(hot=1).order_by('-vacancy_date')
    contacts = Contact.objects.filter(title='Организация')
    return render(request, 'resume/customer.html', {'vacancys': vacancys, 'menuposts': menuposts, 'contacts': contacts})

def join(request):
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    vacancys = Vacancy.objects.filter(hot=1).order_by('-vacancy_date')
    contacts = Contact.objects.filter(title='Организация')
    return render(request, 'resume/recruiter.html', {'vacancys': vacancys, 'menuposts': menuposts, 'contacts': contacts})
