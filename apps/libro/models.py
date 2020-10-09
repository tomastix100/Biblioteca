from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural='autores'
        #L endicamos que ordene por algun atrivuto
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de publicacion', blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    # Este campo se cambiara cada que se cree un registro nuevo o cad que se edite el campo
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True,auto_now_add=False)
    estado = models.BooleanField('Estado', default = True)
    class Meta:
        verbose_name = 'libro'
        verbose_name_plural='libros'
        #L endicamos que ordene por algun atrivuto
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
