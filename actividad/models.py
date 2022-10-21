from django.db import models
from aseguramiento.models import Aseguramiento
from local.models import Local
from tipo_actividad.models import TipoActividad


class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    motivo = models.TextField(blank=True, null=True)
    cantidad_participantes = models.PositiveIntegerField()
    responsable_email = models.EmailField(blank=True, null=True)
    tipo_actividad = models.ForeignKey(to=TipoActividad, on_delete=models.CASCADE,
                                       related_name="actividad_tipoactividad")
    reservaciones = models.ManyToManyField(to=Local, through='Reservacion')
    aseguramientos = models.ManyToManyField(to=Aseguramiento, through='ActividadAseguramiento')

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        db_table = "actividades"

    def __str__(self):
        pass
        init = "Local{"
        end = "}"
        return f"{init} nombre:{self.nombre}, motivo:{self.motivo}, " \
               f"cantidad_participantes:{self.cantidad_participantes}, responsable_email:{self.responsable_email}, " \
               f"tipo_actividad:{str(self.tipo_actividad)}{end}"


class Reservacion(models.Model):
    EstadoChoices = (
        ("Pendiente", "Pendiente"),
        ("Aprobada", "Aprobada"),
        ("Cancelada", "Cancelada"),
    )
    actividad = models.ForeignKey(to=Actividad, on_delete=models.CASCADE, related_name="reservaciones_actividad")
    local = models.ForeignKey(to=Local, on_delete=models.CASCADE, related_name="reservaciones_local")
    estado = models.CharField(max_length=50, choices=EstadoChoices, default="Pendiente")
    fecha_inico = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"
        db_table = "reservacion"

    def __str__(self):
        init = "Reservacion{"
        end = "}"
        return f"{init} actividad:{str(self.actividad)}, local:{str(self.local)}, " \
               f"estado:{self.estado} fecha_inico: {str(self.fecha_inico)}, " \
               f"fecha_fin: {str(self.fecha_fin)}{end}"


class ActividadAseguramiento(models.Model):
    actividad = models.ForeignKey(to=Actividad, on_delete=models.CASCADE,
                                  related_name="actividadaseguramientos")
    aseguramiento = models.ForeignKey(to=Aseguramiento, on_delete=models.CASCADE,
                                      related_name="actividadaseguramientos")
    cantidad = models.PositiveIntegerField()

    class Meta:
        verbose_name = "ActividadAseguramiento"
        verbose_name_plural = "ActividadAseguramientos"
        db_table = "actividad_aseguramiento"

    def __str__(self):
        init = "ActividadAseguramiento{"
        end = "}"
        return f"{init} actividad:{str(self.actividad)}, aseguramiento:{str(self.aseguramiento)}, " \
               f"cantidad:{self.cantidad}{end}"
