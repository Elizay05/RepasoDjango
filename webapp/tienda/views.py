from django.shortcuts import render, redirect
from django.contrib import messages

from tienda.models import *


# Create your views here.


def categorias(request):
    q = Categoria.objects.all()
    context = {'data':q}
    return render (request, 'tienda/categorias/categorias.html', context)

def categorias_form(request):
    return render (request, 'tienda/categorias/categorias_form.html')

def categorias_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        try:
            q = Categoria(
                nombre = nombre,
                descripcion = descripcion
            )
            q.save()
            messages.success(request, f'Categoría creada correctamente!')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('categorias_listar')
    else:
        messages.warning(request, f'Error: no se enviaron datos...')
        return redirect('categorias_listar')

def categorias_eliminar(request, id):
    try:
        q = Categoria.objects.get(pk=id)
        q.delete()
        messages.success(request, f'Categoria eliminada correctamente!')
    except Exception as e:
        messages.error(request, f'Error:{e}')
    return redirect('categorias_listar')

def categorias_form_editar(request, id):
    q = Categoria.objects.get(pk=id)
    context = {'data':q}
    return render(request, 'tienda/categorias/categorias_formulario_editar.html/', context)

def categorias_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Categoria.objects.get(pk=id)
            q.nombre = nombre
            q.descripcion = descripcion
            q.save()
            messages.success(request, f'Categoria actualizada correctamente!')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('categorias_listar')
    else:
        messages.warning(request, f'No se enviaron datos')
        return redirect('categorias_listar')


