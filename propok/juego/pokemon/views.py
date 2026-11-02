from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Entrenadores, Pokemones, Gimnasio

from .forms import (
    EntrenadoresForm,
    PokemonesForm,
    GimnasioForm
)


# ==================================
# CRUD ENTRENADORES
# ==================================

# READ: listar entrenadores
def listar_entrenadores(request):

    entrenadores = Entrenadores.objects.all()

    return render(
        request,
        'pokemon/listar_entrenadores.html',
        {'entrenadores': entrenadores}
    )


# CREATE: registrar entrenador
def crear_entrenador(request):

    if request.method == 'POST':

        formulario = EntrenadoresForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():

            formulario.save()

            return redirect('listar_entrenadores')

    else:

        formulario = EntrenadoresForm()

    return render(
        request,
        'pokemon/formulario_entrenador.html',
        {'formulario': formulario}
    )


# UPDATE: editar entrenador
def editar_entrenador(request, id):

    entrenador = get_object_or_404(
        Entrenadores,
        id=id
    )

    if request.method == 'POST':

        formulario = EntrenadoresForm(
            request.POST,
            request.FILES,
            instance=entrenador
        )

        if formulario.is_valid():

            formulario.save()

            return redirect('listar_entrenadores')

    else:

        formulario = EntrenadoresForm(
            instance=entrenador
        )

    return render(
        request,
        'pokemon/formulario_entrenador.html',
        {
            'formulario': formulario,
            'entrenador': entrenador
        }
    )


# DELETE: eliminar entrenador
def eliminar_entrenador(request, id):

    entrenador = get_object_or_404(
        Entrenadores,
        id=id
    )

    if request.method == 'POST':

        entrenador.delete()

        return redirect('listar_entrenadores')

    return render(
        request,
        'pokemon/eliminar_entrenador.html',
        {'entrenador': entrenador}
    )

# READ: listar pokemones
def listar_pokemones(request):

    pokemones = Pokemones.objects.all()

    return render(
        request,
        'pokemon/listar_pokemones.html',
        {'pokemones': pokemones}
    )


# CREAR: Listar pokemones

# CREATE: registrar pokemon
def crear_pokemon(request):

    if request.method == 'POST':

        formulario = PokemonesForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_pokemones')

    else:
        formulario = PokemonesForm()

    return render(
        request,
        'pokemon/formulario_pokemon.html',
        {'formulario': formulario}
    )

# UPDATE: editar pokemon
def editar_pokemon(request, id):

    pokemon = get_object_or_404(Pokemones, id=id)

    if request.method == 'POST':

        formulario = PokemonesForm(
            request.POST,
            request.FILES,
            instance=pokemon
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_pokemones')

    else:
        formulario = PokemonesForm(instance=pokemon)

    return render(
        request,
        'pokemon/formulario_pokemon.html',
        {
            'formulario': formulario,
            'pokemon': pokemon
        }
    )


# DELETE: eliminar pokemon
def eliminar_pokemon(request, id):

    pokemon = get_object_or_404(Pokemones, id=id)

    if request.method == 'POST':

        pokemon.delete()

        return redirect('listar_pokemones')

    return render(
        request,
        'pokemon/eliminar_pokemon.html',
        {'pokemon': pokemon}
    )

# READ: listar gimnasios
def listar_gimnasios(request):

    gimnasios = Gimnasio.objects.all()

    return render(
        request,
        'pokemon/listar_gimnasios.html',
        {'gimnasios': gimnasios}
    )

# CREATE: registrar gimnasio
def crear_gimnasio(request):

    if request.method == 'POST':

        formulario = GimnasioForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_gimnasios')

    else:
        formulario = GimnasioForm()

    return render(
        request,
        'pokemon/formulario_gimnasio.html',
        {'formulario': formulario}
    )

# UPDATE: editar gimnasio
def editar_gimnasio(request, id):

    gimnasio = get_object_or_404(Gimnasio, id=id)

    if request.method == 'POST':

        formulario = GimnasioForm(
            request.POST,
            request.FILES,
            instance=gimnasio
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_gimnasios')

    else:
        formulario = GimnasioForm(instance=gimnasio)

    return render(
        request,
        'pokemon/formulario_gimnasio.html',
        {
            'formulario': formulario,
            'gimnasio': gimnasio
        }
    )

# DELETE: eliminar gimnasio
def eliminar_gimnasio(request, id):

    gimnasio = get_object_or_404(Gimnasio, id=id)

    if request.method == 'POST':

        gimnasio.delete()

        return redirect('listar_gimnasios')

    return render(
        request,
        'pokemon/eliminar_gimnasio.html',
        {'gimnasio': gimnasio}
    )

# INICIO: pagina principal de ProPok
def inicio(request):

    return render(
        request,
        'pokemon/inicio.html'
    )