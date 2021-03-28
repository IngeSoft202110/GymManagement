from django.urls import path
from polls import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
    path('register/',views.register,name='index'),
    path('main_view/',views.main_view,name='main_view'),

]