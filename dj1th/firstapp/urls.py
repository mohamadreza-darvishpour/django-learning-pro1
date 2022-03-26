from django.urls import path
from . import views


urlpatterns=[
    
#    path("sunday",views.sun),
#    path("saturday",views.sat),
    
    #path("test:<tx>",views.test)   #use place holder
    #path("33<str:tx5>",views.test5),
    #path("22<str:tx4>",views.test4),
    path("cheer",views.cheer_html),
    path("",views.empty_page),
    path("mame<str:tx6>",views.html_page),
    path("<int:tx2>",views.test2),
    path("<str:tx2>",views.test3,name='the-day'),
] 