from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            login(request, user)
            
            return redirect('catalog:product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

