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

def order(request):
    vacancys = Vacancy.objects.filter(activity=1).order_by('-vacancy_date')
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    contacts = Contact.objects.filter(title='Организация')
    if request.method == "POST":
        fb = OrderForms(request.POST)
        if fb.is_valid():
            subject = "Ваше сообщение доставлено"
            body = {
                'name': fb.cleaned_data['name'],
                'surname': fb.cleaned_data['surname'],
                'phone': "Телефон: " + fb.cleaned_data['phone'],
                'telegram': "Телеграм: https://t.me/" + fb.cleaned_data['telegram'],
                'email': "E-mail: " + fb.cleaned_data['email'],
                'country': "Страна " + fb.cleaned_data['country'],
                'company': "Компания: " + fb.cleaned_data['company'],
                'tarif': "Тема вопроса: " + fb.cleaned_data['tarif'],
                'text': "Сообщение: " + fb.cleaned_data['text'],
            }
            text = "\n".join(
                body.values()) + "\n\n___\nКадровое агенство 'Want 2 IT'\n+375255485756\nleomiby@gmail.com\nООО 'Хочу Вайти'"
            try:
                send_mail(subject, text,
                          'a.golubenko@outlook.com',
                          ['want2it@outlook.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            feed = fb.save(commit=False)
            feed.published_date = timezone.now()
            feed.save()
            return redirect('feedback')
    else:
        fb = OrderForms()
    return render(request, 'form.html', {'vacancys': vacancys, 'menuposts':menuposts, 'contacts': contacts})



