from django.db import models

# Create your models here.

class Empleado(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=15, default='Masculino')
    edad = models.IntegerField()
    fecha = models.DateField()
    sueldo = models.FloatField()

    class Meta:
        db_table = 'empleado'  # Especificar el nombre de la tabla que se creara en la migración

    def __str__(self):
        return self.nombre + ' '+ self.apellidos
