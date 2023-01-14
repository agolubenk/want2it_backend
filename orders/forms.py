from django import forms
from .models import Vacancy

class ColorForm(forms.ModelForm):
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control',}))

    class Meta:
        model = Vacancy
        fields = ('color',)
