from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post(request):
    return HttpResponse('we are one')