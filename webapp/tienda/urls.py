from django.urls import path
from . import views

urlpatterns = [
    #CRUD Categorias
    path('categorias_listar/', views.categorias, name='categorias_listar'),
    path('categorias_form/', views.categorias_form, name='categorias_form'),
    path('categorias_crear/', views.categorias_crear, name='categorias_crear'),
    path('categorias_eliminar/<int:id>', views.categorias_eliminar, name='categorias_eliminar'),
    path('categorias_form_editar/<int:id>', views.categorias_form_editar, name='categorias_form_editar'),
    path('categorias_actualizar/', views.categorias_actualizar, name='categorias_actualizar'),
]
