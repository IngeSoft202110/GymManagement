from django.urls import path
from polls import views

urlpatterns = [
    #Views
    path('loginView/',views.loginView,name='loginView'),
    path('',views.index,name='index'),
    path('registerView/',views.registerView,name='registerView'),
    path('mainView/',views.mainView,name='mainView'),
    path('exerciseView/',views.exerciseView,name='exercises'),
    path('exercisesListView/',views.exercisesListView,name='exercisesList'),    
    path('guardarRutinaView/',views.guardarRutinaView,name='guardarRutinaView'),
    path('guardarejerciciosView/',views.guardarejerciciosView, name = 'guardarejerciciosView'),
    path('guardarRutina/', views.guardarRutina, name= 'guardarRutina'),
    #Actions
    path('register/',views.register,name='register'),
    path('main_view/',views.main_view,name='main_view'),
    path('filtrarRutina/',views.filtrarRutina,name='filtrarRutina'),
    path('exercisesList/',views.exercisesList,name='exercisesList'),
]