from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mylove(request):
    return HttpResponse('mylove')