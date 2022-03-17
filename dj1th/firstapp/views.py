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
days={
    'sat':"this is sat",
    'sun':"this is sun",
    'mon':"this is mon",
    'tue':"this is tue",
    'wed':"this is wed",
    'thu':"this is thu",
    'fri':"this is fri",
}

days_by_num=list(days.keys())  #make a list of weekdays.

#important to import httpresponsenotfou..
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect


def test2(request,tx2):
    if int(tx2)<len(days_by_num )  or int(tx2)>len(days_by_num):
        print("test2.one")
        return HttpResponse(f'days {tx2} not found')
    else:
        print("test2.two")
        return HttpResponseRedirect(f'{days_by_num[int(tx2-1)]}')


def test3(request,tx2):
    if tx2 in days.keys():
        print("test3.three")
        return HttpResponse(f'{tx2}->day   {days[tx2]}->data')
    else:
        print("test3.four")
        return HttpResponseNotFound(f'{tx2} is not a weekdays')

