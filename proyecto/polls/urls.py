from django.urls import path
from polls import views

urlpatterns = [
    #Views
    path('',views.index,name='index'),
    path('loginView/',views.loginView,name='loginView'),
    path('registerView/',views.registerView,name='registerView'),
    path('mainView/',views.mainView,name='mainView'),
    path('exerciseView/',views.exerciseView,name='exercises'),
    path('exercisesListView/',views.exercisesListView,name='exercisesList'),
    path('guardarRutinaView/', views.guardarRutinaView, name= 'guardarRutinaView'),
    #Actions
    path('register/',views.register,name='register'),
    path('main_view/',views.main_view,name='main_view'),
    path('filtrarRutina/',views.filtrarRutina,name='filtrarRutina'),
    path('exercisesList/',views.exercisesList,name='exercisesList'),
    path('verComentarios/',views.verComentarios,name='verComentarios'),
    path('verChats/',views.verChats,name='verChats'),
    path('sala/', views.irSala, name='sala'),


    #Ajax
    path('comentar/', views.comentar,name="comentar"),
]