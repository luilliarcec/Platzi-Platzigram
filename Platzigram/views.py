"""Platzigram URL Views """
# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    name = 'Andrés'
    return HttpResponse('Hello world! Esta es la hora señor {name} : {now}'.format(
        name=name,
        now=now
    ))


def sorted_number(request):
    # print(request.method)
    # print(request.path)
    # print(request.GET)
    # print(request.POST)
    # import pdb; pdb.set_trace() Debugger
    numbers = [int(number) for number in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Lista de numeros ordenados'
    }
    # Una manera de responder en json con Django JsonResponse
    # return JsonResponse(data)
    # Otra manera con Django HttpResponse y python json.dumps
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    message = 'Bienvenido {name}'.format(name=name)
    if age < 12:
        message = 'Lo sentimos {name}. Usted no puede entrar aquí.'.format(name=name)
    return HttpResponse(message)
