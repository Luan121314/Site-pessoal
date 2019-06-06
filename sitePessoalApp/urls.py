from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/',views.cursos, name='cursos'),
    path('contato/',views.contato, name='contato'),
    path('saveContato/',views.saveContato, name='saveContato'),
]