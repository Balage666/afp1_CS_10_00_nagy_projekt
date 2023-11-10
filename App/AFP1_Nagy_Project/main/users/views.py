from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
    users_list = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'users_list': users_list,
    }
    return HttpResponse(template.render(context, request))