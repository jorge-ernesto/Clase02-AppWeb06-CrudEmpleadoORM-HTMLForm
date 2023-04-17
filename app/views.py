from django.shortcuts import render, HttpResponse, redirect
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

def home(request):
    return HttpResponse('ya estamos de regreso con Django...')

# funciones para realizar el crud uso de ORM
def listar(request):
    empleados = Empleado.objects.all() # select * from empleados
    contexto = {'empleados':empleados}
    return render(request, 'app/listar.html', contexto)

def agregar(request):
    if request.method == 'POST':
        #crear objeto de la clase empleadoform
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            #grabar empleado
            #El commit = True es opcional, ya que el valor predeterminado de commit es True, revisar el metodo save
            #La mayoría de los desarrolladores usan simplemente form.save() sin especificar el valor de commit, ya que el valor predeterminado de commit es True y los datos se guardan automáticamente en la base de datos.
            #Si commit = False, entonces los datos se mantienen en memoria y no se guardan en la base de datos hasta que se llame manualmente al método save().
            form.save(commit = True) # insert into empleado(....) values(....)
            return redirect('listar')
    else:
        #crear objeto de la clase empleadoform
        form = EmpleadoForm()
    contexto = {'form':form}
    return render(request, 'app/agregar.html',contexto)

def editar(request, empleado_id):
    empleado = Empleado.objects.get(id = empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance = empleado)
        if form.is_valid():
            #grabar empleado
            #El commit = True es opcional, ya que el valor predeterminado de commit es True, revisar el metodo save
            #La mayoría de los desarrolladores usan simplemente form.save() sin especificar el valor de commit, ya que el valor predeterminado de commit es True y los datos se guardan automáticamente en la base de datos.
            #Si commit = False, entonces los datos se mantienen en memoria y no se guardan en la base de datos hasta que se llame manualmente al método save().
            form.save(commit = True) # update empleado set .... where id = ..
            return redirect('listar')
    else:
        #crear objeto de la clase empleadoform
        form = EmpleadoForm(instance = empleado)
    contexto = {'form':form}
    return render(request, 'app/editar.html', contexto)

def eliminar(request, empleado_id):
    empleado = Empleado.objects.get(id = empleado_id)
    #eliminar
    empleado.delete()
    return redirect('listar')
