from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    return render(request,'login.html',context={'msg':'soy el login'})