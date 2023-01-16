from django import forms
from .models import Order

COUNTRY = (
        ('Беларусь', 'Беларусь'),
        ('Россия', 'Россия'),
        ('Казахстан', 'Казахстан'),
        ('США', 'США'),
        ('Польша', 'Польша'),
        ('Германия', 'Германия'),
        ('Великобритания', 'Великобритания'),
        ('Литва', 'Литва'),
        ('Латвия', 'Латвия'),
    )

class OrderForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя',}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Фамилия',}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'375XXYYYYYYY',}))
    country = forms.ChoiceField(choices=COUNTRY, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Страна',}))
    telegram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Telegram',}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Компания',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-mail',}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'placeholder':'Сообщение',}))
    conformation = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch',}))

    class Meta:
        model = Order
        fields = ('name', 'surname', 'phone', 'country', 'telegram', 'company', 'email', 'text', 'conformation')
