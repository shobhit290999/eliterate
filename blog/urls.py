from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("addblog/",views.addblog),#/blog/
    path("blogadd/",views.blogadd),
    path("myblog/",views.myblog),
    path("allblog/",views.allblog),
    path("<str:slug>/",views.parawise),
    
]