from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
