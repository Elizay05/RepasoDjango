from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=254)
    descripcion = models.TextField()

    def str(self):
        return f'{self.nombre}'

class Producto(models.Model):
    nombre = models.CharField(max_length=254, unique=True)
    precio = models.IntegerField()
    inventario = models.IntegerField()
    fecha_creacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def str(self):
        return f'{self.nombre}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=254)
    correo = models.EmailField(max_length=254, unique=True)
    contrasena = models.CharField(max_length=100)
    ROLES = (
        (1, "Administrador"),
        (2, "Despachador"),
        (3, "Cliente"),
    )
    rol = models.IntegerField(choices=ROLES, default=3)
    foto = models.ImageField(upload_to="fotos/")

    def str(self):
        return f'{self.nombre}'