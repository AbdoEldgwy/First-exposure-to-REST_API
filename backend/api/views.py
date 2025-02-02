from django.shortcuts import render
from django.http import JsonResponse

def api_home(request,*arge,**kwargs):
    return JsonResponse({'message': 'Welcome to the API'})
  