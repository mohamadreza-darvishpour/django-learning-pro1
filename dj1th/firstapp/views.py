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
    if int(tx2)<1  or int(tx2)>len(days_by_num):
        print("test2.one")
        return HttpResponse(f'days {tx2} not found')
    else:
        print("test2.two")
        return HttpResponseRedirect(f'{days_by_num[int(tx2-1)]}')


def test3(request,tx2):
    if tx2 in days.keys():
        print("test3.three")
        reply_mes=f'<h3>{tx2}->day   {days[tx2]}->data</h3>'
        return HttpResponse(reply_mes)
    else:
        print("test3.four")
        return HttpResponseNotFound(f'{tx2} is not a weekdays but has been seen here.')

#use html code at response
def html_page(request,tx6):
    html_part = f'<h3> {tx6} will come after mame.joon</h3>'
    return HttpResponse(html_part)

from django.urls import reverse
def empty_page(request):
    data_html=''
    days_list = list(days.keys())
    for d_day in days_list:
        address = reverse('the-day',args=[d_day])
        data_html +=f'''
                    <li>
                        <a href="{address}">{d_day}</a>
                    </li>
                    '''
    return HttpResponse(data_html)



'''
#use reverse and args.
from django.urls import reverse

def test4(request,tx4):
    print("*"*8)
    r_u_one = reverse('the-day',args=[tx4])   #args has should been be in list.
    return HttpResponseRedirect(r_u_one)


def test5(request,tx5):
    re_url=reverse('the-day',args=[tx5])
    print('##'*8)
    return HttpResponseRedirect(re_url)
'''

