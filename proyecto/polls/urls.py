from django.urls import path
from polls import views

urlpatterns = [
    #Views
    path( '' , views.index , name='index'),
    path('loginView/',views.loginView,name='loginView'),
    path('registerView/',views.registerView,name='registerView'),
    path('mainView/',views.mainView,name='mainView'),
    path('exerciseView/',views.exerciseView,name='exercises'),
    path('exercisesListView/',views.exercisesListView,name='exercisesList'),
    path('listaUsuarioView/',views.listaUsuarioView,name='listaUsuarioView'),
    path('verPerfilUsuarioView/',views.verPerfilUsuarioView,name='verPerfilUsuarioView'),

    path('crearRutinaView/',views.crearRutinaView,name = 'crearRutina'),
    path('agregarEjercicioXRutinaView/',views.agregarEjercicioXRutinaView, name = 'agregarEjercicioXRutina'),
    path('agregarEjercicioXRutinaView2/',views.agregarEjercicioXRutinaView2, name ='agregarEjercicioXRutina2'), 
    path('guardarRutinaView/', views.guardarRutinaView,name='guardarRutina'),
    path('exercisesListRutinaView/',views.exercisesListRutinaView,name='exercisesListRutina'),
    path('MiPerfilView/', views.miPerfilView, name='miPerfil'),
    path('actualizarPerfil/', views.actualizarPerfil, name='actualizarPerfil'),
  
    #Actions
    path('register/',views.register,name='register'),
    path('main_view/',views.main_view,name='main_view'),
    path('filtrarRutina/',views.filtrarRutina,name='filtrarRutina'),
    path('exercisesListRutina/',views.exercisesListRutina,name='exercisesListRutina'),
    path('exercisesList/',views.exercisesList,name='exercisesList'),
    path('verComentarios/',views.verComentarios,name='verComentarios'),
    path('verChats/',views.verChats,name='verChats'),
    path('sala/', views.irSala, name='sala'),
    path('dejarSeguirRutina/', views.dejarSeguirRutina, name='dejarSeguirRutina'),
    path('verProgreso/', views.verProgreso, name='verProgreso'),
    path('crearSala/', views.crearSala, name='crearSala'),


    #Ajax
    path('comentar/', views.comentar,name="comentar"),
    path('seguirRutina/', views.seguirRutina,name="seguirRutina"),
    path( 'like/' , views.like , name = "like" ),
    path( 'guardarHistorial/' , views.guardarHistorial , name = "guardarHistorial" ),
]