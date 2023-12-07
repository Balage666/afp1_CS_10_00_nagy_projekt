from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name="bejelentkezes_szukseges")
def users(request):
    users_list = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'users_list': users_list,
    }
    return HttpResponse(template.render(context, request))