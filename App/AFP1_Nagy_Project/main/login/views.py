from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index')
            else:
                messages.error(request, 'Hibás felhasználónév vagy jelszó!')
                return redirect('/login')
        else:
            messages.error(request, 'Hibás adatok!')
            return redirect('/login')
    else:
        form = LoginForm()
        if request.user.is_authenticated:
            message = "A bejelentkezés felület nem elérhető bejelentkezett felhasználóknak!"
            messages.info(request, message)
            return redirect('/index')
    return render(request, 'login.html', {'form': form})
