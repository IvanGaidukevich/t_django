from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=24, min_length=3, required=True)
    first_name = forms.CharField(label='Имя', max_length=24, min_length=2, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=24, min_length=2, required=True)
    email = forms.EmailField(label='Email', max_length=254, required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, required=True)

    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user