from django.urls import path
from . import views


urlpatterns=[
    path('one',views.index1),
    path('two',views.index2),
]