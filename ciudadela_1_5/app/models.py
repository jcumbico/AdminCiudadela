"""
Definition of models.
"""
from django.db import models

# Create your models here.

class Manzana(models.Model):
    Numero = models.IntegerField(unique=True)

class Villa(models.Model):
    Numero = models.IntegerField(unique=True)

class Habitante(models.Model):
    Nombres = models.CharField(max_length= 20)
    Apellidos = models.CharField(max_length=20)
    ManzanaAsignada = models.ForeignKey(Manzana,null=True, on_delete = models.SET_NULL)
    VillaAsignada = models.ForeignKey(Villa,null= True, on_delete=models.SET_NULL)
    Observaciones = models.TextField(null=True)

class Directiva(models.Model):
    Presidente = models.ForeignKey(Habitante,related_name='Directiva_Presidente', null=True, on_delete = models.SET_NULL)
    VicePresidente = models.ForeignKey(Habitante,related_name='Directiva_VicePresidente',null= True, on_delete=models.SET_NULL)
    Secretaria = models.ForeignKey(Habitante,related_name='Directiva_Secretaria',null= True, on_delete=models.SET_NULL)
    Tesorero = models.ForeignKey(Habitante,related_name='Directiva_Tesorero',null= True, on_delete=models.SET_NULL)
    PrimerVocal = models.ForeignKey(Habitante,related_name='Directiva_PrimerVocal',null= True, on_delete=models.SET_NULL)
    SegundoVocal = models.ForeignKey(Habitante,related_name='Directiva_SegundoVocal',null= True, on_delete=models.SET_NULL)
    TercerVocal = models.ForeignKey(Habitante,related_name='Directiva_TercerVocal',null= True, on_delete=models.SET_NULL)
    CuartoVocal = models.ForeignKey(Habitante,related_name='Directiva_CuartoVocal',null= True, on_delete=models.SET_NULL)
    Sindico = models.ForeignKey(Habitante,related_name='Directiva_Sindico',null= True, on_delete=models.SET_NULL)
    FechaDeInicio = models.DateField()
    FechaDeFinalizacion = models.DateField()
    Observaciones = models.TextField(null=True)	

class Proyecto(models.Model):
    Titulo = models.CharField(max_length= 100)
    FechaDeInicioEstimada = models.DateField()
    FechaDeFinalizacionEstimada = models.DateField()
    Beneficiarios = models.TextField(null=True)
    Responsable = models.ForeignKey(Habitante,null= True, on_delete=models.SET_NULL)
    Descripcion = models.TextField(null=True)
    Estado = models.CharField(max_length= 20)
    Observaciones = models.TextField(null=True)

class Evento(models.Model):
    Titulo = models.CharField(max_length= 100)
    Descripcion = models.TextField(null=True)
    FechaDeInicioEstimada = models.DateField()
    HoraDeInicioEstimada = models.TimeField()
    FechaDeFinalizacionEstimada = models.DateField()
    HoraDeFinalizacionEstimada = models.TimeField()
    Beneficiarios = models.TextField(null=True)
    Responsable = models.ForeignKey(Habitante,null= True, on_delete=models.SET_NULL)
    Presupuesto = models.FloatField(null=True)
    Donadores = models.TextField(null=True)
    Gastos = models.FloatField(null=True)
    Programa = models.TextField(null=True)
    Estado = models.CharField(max_length= 20)
    Observaciones = models.TextField(null=True)
    
class Actividad(models.Model):
    ProyectoAsignado = models.ForeignKey(Proyecto,null=True, on_delete = models.SET_NULL)
    EventoAsignado = models.ForeignKey(Evento,null=True, on_delete = models.SET_NULL)
    Fecha = models.DateField()
    Hora = models.TimeField()
    Titulo = models.CharField(max_length= 100)
    Resumen = models.TextField(null=True)
    Descripcion = models.TextField(null=True)
    Responsable = models.ForeignKey(Habitante,null= True, on_delete=models.SET_NULL)
    Foto = models.CharField(max_length= 100)
    DescripcionFoto = models.CharField(max_length= 100)
    Observaciones = models.TextField(null=True)

class TipoRegistroDeDinero(models.Model):
    Titulo = models.CharField(max_length= 100)
    Categoria = models.CharField(max_length= 20)
    Observaciones = models.TextField(null=True)

class RegistroIngresoEgreso(models.Model):
    Tipo = models.ForeignKey(TipoRegistroDeDinero,null=True, on_delete = models.SET_NULL)
    Valor = models.FloatField(null=True)
    ManzanaAsignada = models.ForeignKey(Manzana, null=True, on_delete = models.SET_NULL)
    VillaAsignada = models.ForeignKey(Villa, null=True, on_delete = models.SET_NULL)
    Fecha = models.DateField()
    Descripcion = models.TextField(null=True)
    Evidencia = models.CharField(max_length= 100)
    Observaciones = models.TextField(null=True)

class rptRendicionDeCuentas(models.Model):
    Orden = models.PositiveSmallIntegerField(null=True)
    Anio = models.PositiveSmallIntegerField(null=True)
    MesNombre = models.CharField(max_length=20)
    Tipo = models.CharField(max_length=100)
    Titulo = models.CharField(max_length=100)
    Valor = models.FloatField(null=True)

class Encuesta(models.Model):
    Anio  = models.PositiveSmallIntegerField(null=True)
    Mes  = models.PositiveSmallIntegerField(null=True)
    Positivo = models.FloatField(null=True)
    Negativo = models.FloatField(null=True)
    Observaciones = models.TextField(null=True)

class Queja(models.Model):
    Persona = models.ForeignKey(Habitante,null=True, on_delete = models.SET_NULL)
    Fecha = models.DateField()
    Descripcion = models.TextField(null=True)
    Evidencia = models.CharField(max_length= 100)
    Valor = models.FloatField(null=True)
    Observaciones = models.TextField(null=True)

class Negocio(models.Model):
    Titulo = models.CharField(max_length= 100)
    Longitud = models.FloatField(null=True)
    Latitud = models.FloatField(null=True)
    Descripcion = models.TextField(null=True)
    Foto = models.CharField(max_length= 100)
    Observaciones = models.TextField(null=True)
