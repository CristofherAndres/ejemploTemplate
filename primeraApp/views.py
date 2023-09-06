from django.shortcuts import render

# Create your views here.
def llamarTemplate(request):
    return render(request, 'primeraApp/primerTemplate.html')


def infoUsuario(request):
    data = {
        'nombre': 'Pedro',
        'apellido': 'Parker',
        'correo': 'peterparker@dayli.cl',
        'direccion': 'New York, Casa tia May',
        
    }
    return render(request, 'primeraApp/segundoTemplate.html',data)