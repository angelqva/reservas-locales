from django.db import models


class TipoActividad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "TipoActividad"
        verbose_name_plural = "TipoActividades"
        db_table = "tipo_actividades"

    def __str__(self):
        init = "TipoActividad{"
        end = "}"
        return f"{init} codigo:{self.codigo}, nombre:{self.nombre}, " \
               f"descripción:{self.descripcion}{end}"
