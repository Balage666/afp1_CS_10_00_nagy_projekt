from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required(redirect_field_name="bejelentkezes_szukseges")
def index(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'index.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def documentation(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'documentation.html', {'message': message})
    else:
        return render(request, 'documentation.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def trello_cards(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'trello_cards.html', {'message': message})
    else:
        return render(request, 'trello_cards.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def code(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'code.html', {'message': message})
    else:
        return render(request, 'code.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def profile(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'profile.html', {'message': message})
    else:
        return render(request, 'profile.html') 

@login_required(redirect_field_name="bejelentkezes_szukseges")
def logout_view(request):
    logout(request)
    return redirect('login')