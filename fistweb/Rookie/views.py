from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from .form import NameForm


# Create your views here.
# 主页
def home(request):
    return render(request, 'home.html')


# # 登录页
# def user_login(request):
#     return render(request, 'log_on.html')

    # 文件上传
    # def upfile(request):
    # if request.method=="post" :
    #     myfile = request.FILES.get("myfile",None)
    #     if not myfile:
    #         return HttpResponse("error")
    #     destionation =open()
    pass


# 用户登录
def user_logon(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["name"], password=request.POST["password"])
        if user is None:
            return render(request, 'log_on.html', {"error": "用户名或密码错误"})
        else:
            login(request, user)
            return render(request,"logon_win.html")
            # return HttpResponse("error")
    else:
        return render(request,'log_on.html')
        # return HttpResponse("file 登录错误")
