from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = SignUpForm()
        if request.user.is_authenticated:
            message = "A regisztrációs felület nem elérhető bejelentkezett felhasználóknak!"
            messages.info(request, message)
            return redirect('/index')
    return render(request, "register.html", {"form": form})
