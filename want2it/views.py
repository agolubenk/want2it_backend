from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog
from vacancy.models import Vacancy
from contacts.models import Contact


def page_not_found_view(request, exception):
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    vacancys = Vacancy.objects.filter(activity=1).order_by('-vacancy_date')
    contacts = Contact.objects.filter(title='Организация')
    return render(request, '404.html', {'menuposts': menuposts, 'vacancys': vacancys, 'contacts': contacts}, status=404)

