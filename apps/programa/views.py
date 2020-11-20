from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import ProgramaForm, AsignacionBeneficioForm
from .models import Programa, AsignacionBeneficio


def programa_lista(request):
    programas = Programa.objects.all()
    return render(request, 'programa/lista.html',
                  {'programas': programas})


def programa_detalle(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    return render(request,
                  'programa/detalle.html',
                  {'programa': programa})


def programa_create(request):
    nuevo_programa = None
    if request.method == 'POST':
        programa_form = ProgramaForm(request.POST, request.FILES)
        if programa_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_programa = programa_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_programa))
            return redirect(reverse('programa:programa_detalle', args={nuevo_programa.id}))
    else:
        programa_form = ProgramaForm()

    return render(request, 'programa/programa_form.html',
                  {'form': programa_form})


def programa_delete(request):
    if request.method == 'POST':
        if 'id_programa' in request.POST:
            programa = get_object_or_404(Programa, pk=request.POST['id_programa'])
            nombre_programa = programa.nombre
            programa.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Programa {}'.format(nombre_programa))
        else:
            messages.error(request, 'Debe indicar qué Programa se desea eliminar')
    return redirect(reverse('programa:programa_lista'))


def programa_edit(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    if request.method == 'POST':
        form_programa = ProgramaForm(request.POST, request.FILES, instance=programa)
        if form_programa.is_valid():
            form_programa.save()
            messages.success(request, 'Se ha actualizado correctamente el Programa')
            return redirect(reverse('programa:programa_detalle', args=[programa.id]))
    else:
        form_programa = ProgramaForm(instance=programa)

    return render(request, 'programa/programa_edit.html', {'form': form_programa})

#Generar una vista y templates correspondientes para realizar la asignación del beneficio a la persona.

def asignar_beneficio(request):
    nuevo_beneficio = None
    if request.method == 'POST':
        nuevo_beneficio = AsignacionBeneficioForm(request.POST)
        if nuevo_beneficio.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            beneficio = nuevo_beneficio.save(commit=True)
            messages.success(request,'Beneficio asignado con éxito'.format(beneficio))
            return redirect('home')
    else:
        nuevo_beneficio = AsignacionBeneficioForm()

    return render(request, 'asignacionBeneficio.html', {'form': nuevo_beneficio})

#Generar una vista y templates para mostrar un listado de los beneficios asignados para un Programa 
# y rango de fechas en particular.

def buscar_beneficios(request, pk):
    programa = get_object_or_404(Programa, pk=pk)

    return render(request, 'buscarBeneficios.html',{'programa': programa})    

def lista_beneficios(request,pk):
    programa = get_object_or_404(Programa, pk=pk)
    beneficios = None
    fecha_inicio=None
    if request.method == 'POST':
            fecha_inicio = request.POST['fecha_inicio']
            fecha_fin = request.POST['fecha_fin']
            #ahora buscamos fechas
            beneficios = AsignacionBeneficio.objects.filter(programa_id = programa.id).filter(fecha_entrega__gte = fecha_inicio).filter(fecha_entrega__lte=fecha_fin)
    return render(request, 'listaBeneficios.html', {'programa':programa,'beneficios': beneficios})
