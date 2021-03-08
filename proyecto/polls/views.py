from django.shortcuts import render
from django.http import HttpResponse
def loggin(request):
    return render(request,'loggin.html',context={'msg':'soy el loggin'})