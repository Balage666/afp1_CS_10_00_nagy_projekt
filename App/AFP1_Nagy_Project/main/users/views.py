from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def is_superuser(user):
    return user.is_superuser if user.is_authenticated else False

@login_required(redirect_field_name="bejelentkezes_szukseges")
@user_passes_test(is_superuser, login_url='/index', redirect_field_name="jogosultsag_szukseges")
def users(request):
    users_list = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'users_list': users_list,
    }
    return HttpResponse(template.render(context, request))