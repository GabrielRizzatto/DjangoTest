from django.http import HttpResponse
from django.shortcuts import render


def blog (request):
    return HttpResponse('Blog')

def exemplo (request):
    return HttpResponse('Exemplo')