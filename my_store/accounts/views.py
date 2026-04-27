from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserCreationForm



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

