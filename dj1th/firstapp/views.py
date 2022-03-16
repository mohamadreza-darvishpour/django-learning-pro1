from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
'''
def sat(request):
    return HttpResponse("saturday")
def sun(request):
    return HttpResponse("sunday...")
'''

#make dynamic url: to use placeholder...
'''
def test(request,tx):
    return HttpResponse("hello dear. remember %s..."%tx)
'''
#make dynamic url by dict and place holder
days={'wed':"this is sat",
'thurs':"thurs is thurs",
'fri':"this is fri",
}
#important to import httpresponsenotfou..
from django.http import HttpResponseNotFound
def test2(request,tx2):
    data1=days.get(f'{tx2}')
    if data1==None:
        return HttpResponseNotFound("page has not been founded! try again.")
    return HttpResponse(f'day:{tx2}  data:{data1}')
