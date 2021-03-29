from django.urls import path
from polls import views

urlpatterns = [
    #Views
    path('loginView/',views.loginView,name='loginView'),
    path('',views.index,name='index'),
    path('registerView/',views.registerView,name='registerView'),
    path('mainView/',views.mainView,name='mainView'),

    #Actions
    path('register/',views.register,name='register'),

]