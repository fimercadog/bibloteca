from django.db import models


# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombres', max_length=200)
    apellidos = models.CharField('Apellidos', max_length=220)
    nacionalidad = models.CharField('Nacionalidad', max_length=100)
    descripcion = models.CharField('Descripción', max_length=600, blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=255)
    fecha_publicacion = models.DateField('Fecha de publicación')
    # autor_id = models.OneToOneField(Autor,on_delete=models.CASCADE)  # 1 - 1
    # autor_id = models.ForeignKey(Autor,on_delete=models.CASCADE)  # 1 - M
    autor_id = models.ManyToManyField(Autor)  # M - M
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
