from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login as auth_login  # to avoid conflict with login function in views.py


def login(request, user):
    return render(request, 'registration/login.html', {'user': user})

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('shop:product_list')
        else:
            return render(request, 'registration/signup.html', {'form': form})
