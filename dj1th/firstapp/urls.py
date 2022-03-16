from django.urls import path
from . import views


urlpatterns=[
    
#    path("sunday",views.sun),
#    path("saturday",views.sat),
    
    #path("test:<tx>",views.test)   #use place holder
    path("<tx2>",views.test2),
] 