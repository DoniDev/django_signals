from django.http import HttpResponse
from django.shortcuts import render


'''
    Django Signals are comprised of senders and recievers
    
    
    Types
    1.Modal Signals
    
'''


def home(request):
    return HttpResponse('Hello, World!')
