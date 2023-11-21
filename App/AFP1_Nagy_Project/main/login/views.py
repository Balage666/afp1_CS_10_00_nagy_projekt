from django.shortcuts import render, redirect
from users.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('/index')
        except User.DoesNotExist:
            error_message = 'Hibás felhasználónév vagy jelszó.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')