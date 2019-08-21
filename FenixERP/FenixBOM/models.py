from django.db import models




class cliente(models.Model):
    Nombre = models.CharField(max_length=100, null=False)
    Descripcion  = models.CharField(max_length=200)

class partNumTipo(models.Model):
    tipoNom = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=20)

class maqPros(models.Model):
    Nombre  = models.CharField(max_length=200, null= False)
    Descripcion = models.CharField(max_length=200)


class partNumb(models.Model):
    PartCode = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=500)
    partnumt = models.ManyToOneRel(partNumTipo, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    #cliente =

class partBom(models.Model):
    PartCode = models.OneToOneRel(partNumb, on_delete=models.CASCADE())
    Descipcion = models.CharField(max_length=200)
    Version = models.IntegerField(null=False)
    Fecha = models.DateField(null=False)
    Componentes = models.ManyToManyRel()

class partRoutes(models.Model):
    PartCode = models.ManyToManyRel(partNumb)
    BOM = models.ManyToManyRel(partBom)
    MaPros = models.ManyToManyRel(maqPros)
    Version = models.IntegerField(null=False)

class dibujo(models.Model):
    PartCode = models.OneToOneRel(partNumb, on_delete=models.CASCADE())
    Descripcion =  models.CharField(max_length=200)
    #dibujo = models.FileField()
    Version = models.IntegerField(null=False)
# Create your models here.
