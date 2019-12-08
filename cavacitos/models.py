from django.db import models


class Oferente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        'Nombres de Oferente', max_length=200, null=True, blank=False)
    apellidos = models.CharField(
        'Apellidos de Oferente', max_length=200, null=False, blank=False)
    turno = models.CharField(
        'Turno del Oferente', max_length=200, null=False, blank=False)
    dia = models.CharField(
        'Dia de Oferente', max_length=200, null=False, blank=False)
    pago = models.IntegerField()
    telefono = models.IntegerField()
    colonia = models.CharField(
        'Colonia de Oferente', max_length=200, null=False, blank=False)
    superficie = models.IntegerField()
    correo = models.EmailField('Correo Electronico', null=False, blank=False)
    estadoDiscapacidad = models.BooleanField(
        'Con Discapacidad/ Sin Discapacidad ', default=False)
    estadoAM = models.BooleanField(
        'Si Adulto Mayor/ No Adulto Mayor ', default=False)
    estadoTirado = models.BooleanField('Si Tirado/ No Tirado ', default=False)
    nombres = models.CharField(
        'Giro de Oferente', max_length=200, null=False, blank=False)
    tipoPermiso = models.CharField(
        'Tipo de Permiso', max_length=200, null=False, blank=False)
    tipoPermiso = models.CharField(
        'Mercado Correspondiente', max_length=200, null=False, blank=False)
    fecha_creacion = models.DateField(
        'Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Oferente'
        verbose_name_plural = 'Oferentes'

    def __str__(self):
        return self.nombre


class Inspector(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        'Nombre Inspector', max_length=100, null=False, blank=False)
    contrasena = models.CharField(
        'Contraseña Inspector', max_length=100, null=False, blank=False)
    fecha_creacion = models.DateField(
        'Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Inspector'
        verbose_name_plural = 'Inspectores'

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        'Nombre Inspector', max_length=100, null=False, blank=False)
    contrasena = models.CharField(
        'Contraseña Inspector', max_length=100, null=False, blank=False)
    fecha_creacion = models.DateField(
        'Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.nombre
