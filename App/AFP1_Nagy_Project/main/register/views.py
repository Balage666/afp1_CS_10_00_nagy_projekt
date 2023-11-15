from django.shortcuts import render, redirect
from users.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                new_user = User(username=username, password=password)
                new_user.save()
                return redirect('/login')
            else:
                error_message = 'A felhasználónév már foglalt.'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'A jelszavak nem egyeznek meg.'
            return render(request, 'register.html', {'error_message': error_message})
            
    return render(request, 'register.html')
