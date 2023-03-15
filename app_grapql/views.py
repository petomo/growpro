#import requests
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .models import User
from graphql_auth.models import UserStatus
from graphql_auth.utils import get_token_paylod
from graphql_auth.settings import graphql_auth_settings as app_settings
from graphql_auth.constants import TokenAction
#from graphql_jwt.shortcuts import get_token
#from graphql_jwt.refresh_token.utils import get_refresh_token_model #TokenModel
UserModel = get_user_model()
urlfe="http://127.0.0.1:5000/"
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, template_name='index.html',context={'name':'thong'})

def activate(request,token):
    #UserStatus.verify(token)
    payload = get_token_paylod(token, TokenAction.ACTIVATION, app_settings.EXPIRATION_ACTIVATION_TOKEN)
    user = UserModel._default_manager.get(**payload)
    user_status = UserStatus.objects.get(user=user)
    if user_status.verified is True:
        return redirect("%sverify"%urlfe)
    elif user_status.verified is False:
        user_status.verified = True
        user_status.save(update_fields=["verified"])
        return redirect("%sverify"%urlfe)
    else:
        return render(request, template_name='index.html',context={'name':'lỗi'})

def resetPass(request,token):
    payload = get_token_paylod(token, TokenAction.PASSWORD_RESET, app_settings.EXPIRATION_PASSWORD_RESET_TOKEN)
    user = UserModel._default_manager.get(**payload)
    if user:
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save()
        url=urlfe+"getpass?s="+password
        return redirect(url)
    return render(request, template_name='index.html',context={'name':'lỗi'})
    
    