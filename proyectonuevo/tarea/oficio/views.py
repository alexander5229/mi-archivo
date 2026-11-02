

from django.shortcuts import render, redirect, get_object_or_404
from .models import Aprendiz
from .forms import AprendizForm


# READ: Consultar y mostrar aprendices
def lista_aprendices(request):

    aprendices = Aprendiz.objects.select_related('Programa').all()

    contexto = {
        "aprendices": aprendices
    }

    return render(
        request,
        "lista_aprendices.html",
        contexto
    )


# CREATE: Registrar un nuevo aprendiz
def crear_aprendiz(request):

    if request.method == 'POST':

        formulario = AprendizForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_aprendices')

    else:
        formulario = AprendizForm()

    contexto = {
        'formulario': formulario
    }

    return render(
        request,
        'crear_aprendiz.html',
        contexto
    )

def editar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)

    if request.method == 'POST':
        formulario = AprendizForm(request.POST, instance=aprendiz)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_aprendices')
    else:
        formulario = AprendizForm(instance=aprendiz)

    return render(request, 'crear_aprendiz.html', {
        'formulario': formulario,
        'titulo': 'Editar aprendiz'
    })


# DELETE: Eliminar aprendiz
def eliminar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)

    if request.method == 'POST':
        aprendiz.delete()
        return redirect('lista_aprendices')

    return render(request, 'eliminar_aprendiz.html', {
        'aprendiz': aprendiz
    })
