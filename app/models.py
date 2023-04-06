from django.db import models

# Crear la clase Empleado.
class Empleado(models.Model):
    #definir los campos de la clase
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    sexo=models.CharField(max_length=15,default='Masculino')
    edad=models.IntegerField()
    fecha=models.DateField()
    sueldo=models.FloatField()

    class Meta:
        db_table='empleado'
        

    def __str__(self):
        return self.nombre + ' '+self.apellidos
    

