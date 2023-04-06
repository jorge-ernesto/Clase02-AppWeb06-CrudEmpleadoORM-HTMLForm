from django.shortcuts import render,HttpResponse,redirect
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.
def home(request):
    return HttpResponse('ya estamos de regreso con Django...')

# funciones para realizar el crud uso de ORM
def listar(request):
    empleados=Empleado.objects.all() # select * from empleados
    contexto={'empleados':empleados}
    return render(request,'app/listar.html',contexto)

def agregar(request):
    if request.method=='POST':
        #crear objeto de la clase empleadoform
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            #grabar empleado
            form.save(commit=True) # insert into empleado(....) values(....)
            return redirect('listar')
    else:
        #crear objeto de la clase empleadoform
        form=EmpleadoForm()
    contexto={'form':form}
    return render(request,'app/agregar.html',contexto)

def editar(request,empleado_id):
    empleado=Empleado.objects.get(id=empleado_id)
    if request.method=='POST':
        form=EmpleadoForm(request.POST,instance=empleado)
        if form.is_valid():
             #grabar empleado
            form.save(commit=True) # update empleado set .... where id=..
            return redirect('listar')
    else:
        #crear objeto de la clase empleadoform
        form=EmpleadoForm(instance=empleado)
    contexto={'form':form}
    return render(request,'app/editar.html',contexto)

def eliminar(request,empleado_id):
     empleado=Empleado.objects.get(id=empleado_id)
     #eliminar
     empleado.delete()
     return redirect('listar')



