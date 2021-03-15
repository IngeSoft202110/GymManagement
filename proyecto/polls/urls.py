from django.urls import path
from polls import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
    path('signin/',views.signin,name='index'),

]