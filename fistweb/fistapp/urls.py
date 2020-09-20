from django.urls import path
from . import views,search,message
urlpatterns = [
    # path(r'', message.message),
    # url(r'^testdb$', testdb.testdb),
    #    用来指向留言板
    path('message_form/', message.message_form),
    path('message/', message.message),
    path('find_book/', message.find_book)
]