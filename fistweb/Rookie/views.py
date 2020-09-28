from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .form import NameForm
from . import models


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
        user = models.custom.objects.filter(user=request.POST["user"])
        print("-----------------------", request.POST["user"])
        # user = authenticate(request, username=request.POST["user"], password=request.POST["password"])
        print("-----------------------", user)
        if user:
            error = "user不是空 登陆成功界面可访问"
            if request.POST["password"] == user[0].password:
                return render(request, 'Logon_win.html', {"error": error})
                # return redirect(request,'/Logon_win/')
            else:
                error = "user正确 密码错误"
                return render(request, 'Logon_file.html',{"error":error})
            print("user不是空")
        else:
            print("user是空")
            error = "user是空 注册界面可访问"
            # render(request, 'register.html', {"error": error})

            return redirect('/register/')
    else:
        error = "user是空 登录界面可访问"
        return render(request, 'Log_on.html', {"error": error})
        # return HttpResponse("file 登录错误")


def register(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        custom_new = models.custom(user=username, password=password)
        custom_new.save()
        error = "注册成功"
        return redirect('/logon/')
    else:
        error = "欢迎注册"
        return render(request, 'register.html', {"error": error})
