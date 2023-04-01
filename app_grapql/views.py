#import requests
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from graphql_auth.models import UserStatus
from graphql_auth.utils import get_token_paylod
from graphql_auth.settings import graphql_auth_settings as app_settings
from graphql_auth.constants import TokenAction
from django.core.files.base import ContentFile,File
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponse,JsonResponse
from .models import User,HistoryFileUp
import os
#from graphql_jwt.shortcuts import get_token
#from graphql_jwt.refresh_token.utils import get_refresh_token_model #TokenModel
UserModel = get_user_model()
urlfe="http://127.0.0.1:5000/"


# Create your views here.


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

@csrf_exempt    
def uploadFile(request):
    if request.method == 'POST':
        file = request.FILES['file']
        _file=file.read()
        content_file = ContentFile(_file)
        _filename=request.POST['filename']
        _typefile=request.POST['filetype']
        
        if content_file:
            user=User.objects.get(username=request.POST['user'])
            if user:
                _size=len(content_file)
                _files_old=HistoryFileUp.objects.filter(size=_size)
                if _files_old:
                    for p in _files_old:
                        current_dir=""
                        url = os.path.abspath(os.path.join(current_dir, os.pardir))+"/growpro/app_grapql%s"%p.file.url
                        if os.path.isfile(url):
                            with open(url,'rb') as f:
                                if _file == f.read():
                                    result = {'status': True,'url':p.file.url,'message':'file exists'}  
                                    return JsonResponse(result) 
                uploaded_file = UploadedFile(
                    file=content_file, 
                    name=_filename,
                    content_type=_typefile
                )
                fileUpload=HistoryFileUp.objects.create(
                    title=_filename,
                    user=user,
                    file=uploaded_file,
                    typefile=_typefile,
                    size=_size
                ) 
                result = {'status': True,'url':fileUpload.file.url,'message':'saved files'}                  
            else:result = {'status': False,'url':None,'message':'user does not exist'}    
        else:result = {'status': False,'url':None,'message':'file does not exist'}  
        return JsonResponse(result)  
    return 
