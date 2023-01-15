from django import forms
from .models import Order

class OrderForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя',}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Фамилия',}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Контактный номер',}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Страна',}))
    telegram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Telegram',}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Компания',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-mail',}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'placeholder':'Сообщение',}))

    class Meta:
        model = Order
        fields = ('name', 'surname', 'phone', 'country', 'telegram', 'company', 'email', 'text')