from django.urls import path
from polls import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('home/',views.index,name='index'),
]