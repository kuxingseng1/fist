from django.urls import path
from . import views

app_name = "Rookie"
urlpatterns = [
    # path("python/",views.rookie),
    # # 文件传输url
    # path("upfile/",views.upfile),
    # # 登录url
    path("home/", views.home,name='home'),
    path("logon/", views.user_logon, name='user_logon'),
]
