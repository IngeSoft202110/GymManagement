from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    return render(request,'login.html',context={'msg':'soy el login'})
def index(request):
    return render(request,'index.html',context={'msg':'HOME'})

def main_view(request):
    return render(request,'main_view.html',context={})

def register(request):
    return render(request,'register.html',context={'msg':'SIGN IN'})