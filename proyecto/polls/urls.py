from django.urls import path
from polls import views

urlpatterns = [
    path('loggin/',views.loggin,name='login'),
]