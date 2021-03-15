from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    return render(request,'login.html',context={'msg':'soy el login'})
def index(request):
    return render(request,'index.html',context={'msg':'HOME'})



def signin(request):
    return render(request,'signin.html',context={'msg':'SIGN IN'})