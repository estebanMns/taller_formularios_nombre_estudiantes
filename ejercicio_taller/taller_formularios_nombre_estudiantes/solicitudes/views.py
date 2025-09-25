from django.shortcuts import render, redirect
from .forms import SolicitudForm

def crear_solicitud(request):
    """
    Vista para crear una nueva solicitud.
    """
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitud_exitosa')
    else:
        form = SolicitudForm()
    
    context = {'form': form}
    return render(request, 'solicitudes/crear_solicitud.html', context)

def solicitud_exitosa(request):
    """
    Vista para mostrar un mensaje de éxito después de enviar el formulario.
    """
    return render(request, 'solicitudes/solicitud_exitosa.html')
