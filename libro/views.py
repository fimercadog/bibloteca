from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from libro.forms import *
from libro.models import *


# Create your views here.
def HomeView(request):
    return render(request, 'index.html')


def crearAutorView(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            # nom=autor_form.cleaned_data['nombre']
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
        # print(autor_form)
        # print(request.POST)
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})

# def crearAutorView(request):
#     if request.method == 'POST':
#         # print(request.POST)
#         nom = request.POST.get('nombre')
#         ape = request.POST.get('apellidos')
#         nacio = request.POST.get('nacionalidad')
#         desc = request.POST.get('descripcion')
#         autor = Autor(nombre=nom, apellidos= ape, nacionalidad= nacio,descripcion= desc)
#         autor.save()
#         return redirect('index')
#     render(request, 'libro/crear_autor.html')


def listarAutorView(request):
    # autores = Autor.objects.all()
    autores = Autor.objects.filter(estado=True)
    return render(request, 'libro/listar_autor.html', {'autores': autores})


def editarAutorView(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)  # get trae 1 - filter trae una lista
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})


# eliminar logica
def eliminarAutorView(request, id):
    autor = Autor.objects.get(id=id)
    autor.estado = False
    autor.save()
    return redirect('libro:listar_autor')

# eliminar mediante metodo post
# def eliminarAutorView(request, id):
#     autor = Autor.objects.get(id=id)
#     if request.method == 'POST':
#         autor.delete()
#         return redirect('libro:listar_autor')
#     return render(request, 'libro/eliminar_autor.html', {'autor': autor})

# eliminar mediante metodo get
# def eliminarAutorView(request, id):
#     autor = Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('libro:listar_autor')
