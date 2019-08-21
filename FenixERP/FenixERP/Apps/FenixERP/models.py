from django.db import models

# Create your models here.

class Tienda(models.Model):

    Nombre = models.CharField(max_length=100)
    Calle = models.CharField(max_length=50, null=False, blank=False)
    Numero = models.CharField(max_length=4, null=False, blank=False)
    Colonia = models.CharField(max_length=50, null=False, blank=False)
    Municipio = models.CharField(max_length=50, null=False, blank=False)
    Estado = models.CharField(max_length=50, null=False, blank=False)
    codigoPostal = models.CharField(max_length=6, null=False, blank=False)
    urlDireccion = models.CharField(max_length=600, null=False, blank=False)
    FechaRegistro = models.DateField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.Nombre)

    def direccion(self):
        return "Calle {0} numero {1} colonia {2}".format(self.Calle, self.Numero, self.Colonia)




class MarcaAuto(models.Model):
    Nombre = models.CharField(max_length=50, null=False, blank=False)
    Descripcion = models.CharField(max_length=50, default="Sin descripcion")

    def __str__(self):
        return "{0}".format(self.Nombre)

class MarcaProducto(models.Model):
    Nombre = models.CharField(max_length=50, null=False, blank=False)
    Descripcion = models.CharField(max_length=50, default="Sin descripcion")

    def __str__(self):
        return "{0}".format(self.Nombre)

class Auto(models.Model):
    Modelo = models.CharField(max_length=50)
    MarcAuto = models.ForeignKey(MarcaAuto, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} modelo: {1}".format(self.MarcAuto, self.Modelo)


class ProductoTienda(models.Model):
    Tienda = models.ForeignKey(Tienda, null=False, blank=False, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    MarcaProd = models.ForeignKey(MarcaProducto, null=False, blank=False, on_delete=models.CASCADE)
    RefaccionDe = models.ManyToManyField(Auto)
    Descripcion = models.CharField(max_length=200, default="Sin descripcion")
    imagen = models.ImageField(upload_to="images/")
    Activo = models.BooleanField(default=True)

    def __str__(self):
        return "{0}".format(self.Nombre)


