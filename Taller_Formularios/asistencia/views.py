from django.shortcuts import render, redirect, get_object_or_404
from .forms import AsistenciaForm
from .models import Asistencia
from django.urls import reverse

def lista_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'asistencia/asistencia_list.html', {'asistencias': asistencias})

def crear_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia:list')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencia/asistencia_form.html', {'form': form})

def detalle_asistencia(request, pk):
    a = get_object_or_404(Asistencia, pk=pk)
    return render(request, 'asistencia/asistencia_detail.html', {'asistencia': a})
