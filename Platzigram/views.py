"""Platzigram URL Views """
# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    name = 'Andrés'
    return HttpResponse('Hello world! Esta es la hora señor {name} : {now}'.format(
        name=name,
        now=now
    ))


def hi(request):
    # print(request.method)
    # print(request.path)
    # print(request.GET)
    # print(request.POST)
    # import pdb; pdb.set_trace() Debugger
    numbers = request.GET['numbers']
    return JsonResponse(numbers, safe=False)
    # return HttpResponse('Hi! {}'.format(str(numbers)))
