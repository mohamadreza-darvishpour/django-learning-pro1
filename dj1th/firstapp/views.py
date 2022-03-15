from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def index1(request):
    return HttpResponse("hi i start the django... continue till death.")

def index2(request):
    return HttpResponse("you are good man...")