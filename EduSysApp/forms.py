from django import forms
from .models import *
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=20)
    password = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput)
    first_name = forms.CharField(label='Имя', max_length=50)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    middle_name = forms.CharField(label='Отчество', max_length=50, required=False)
    phone_number = forms.CharField(label='Номер телефона', max_length=11, required=False)
    email = forms.EmailField(label='Email', max_length=100, required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=20)
    password = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput)