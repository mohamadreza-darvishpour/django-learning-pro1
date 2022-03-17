from django.urls import path
from . import views


urlpatterns=[
    
#    path("sunday",views.sun),
#    path("saturday",views.sat),
    
    #path("test:<tx>",views.test)   #use place holder

    path("<int:tx2>",views.test2),
    path("<str:tx2>",views.test3),
] 