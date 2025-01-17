from django.db import models
from django.template.defaulttags import register
from module_resources.models import Hospital, Servicio, Vehiculo
from django.contrib.auth.models import User

SERVICE_CHOICE = (
    ('telefono', 'Teléfono'),
    ('personal', 'Personal')
)

class Reporte(models.Model):
    # ****** DATOS DEL REPORTE ******
    control = models.IntegerField(blank=False)
    fecha_reporte = models.DateField(blank=False, verbose_name='Fecha de reporte')
    salida = models.CharField(max_length=256, blank=False, verbose_name='Salida a')
    hora_salida = models.DateTimeField(blank=False, verbose_name='Hora de salida')
    entrada = models.CharField(max_length=256, blank=False, verbose_name='Entrada a')
    hora_entrada = models.DateTimeField(blank=False, verbose_name='Hora de entrada')
    observaciones = models.TextField(blank=True)

    # DATOS DEL PERSONAL
    pilotos = models.ManyToManyField(User, verbose_name='Piloto(s)')
    radiotelefonista = models.ForeignKey(User, related_name='telefonista', on_delete=models.PROTECT)
    unidades = models.ManyToManyField(Vehiculo, verbose_name='Unidad(es)')
    personal_destacado = models.ManyToManyField(User, related_name='personal', verbose_name='Personal Destacado')

    # DATOS DEL SERVICIO
    tipo_solicitud = models.CharField(max_length=10, choices=SERVICE_CHOICE, verbose_name='Tipo de solicitud')
    direccion = models.CharField(blank=False, max_length=256, verbose_name='Dirección')
    solicitantes = models.TextField(blank=False)
    pacientes = models.TextField(blank=True)
    fallecidos = models.TextField(blank=True)
    domicilios = models.TextField(blank=False)
    escoltas = models.TextField(blank=True, verbose_name='Acompañantes')
    tipo_servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, verbose_name='Tipo de servicio')
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, verbose_name='Hospital de traslado')

    @register.filter(is_safe=True)
    def clabel(value):
        return value.label_tag(attrs={'class': 'form-label'})
