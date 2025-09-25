from django.shortcuts import render
from .forms import AsistenciaForm


def registro_asistencia(request):
    form = AsistenciaForm()
    context = {'form': form}
    return render(request, 'asistencia/registro_asistencia.html', context)