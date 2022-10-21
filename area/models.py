from django.db import models


class Area(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        db_table = "areas"

    def __str__(self):
        init = "Area{"
        end = "}"
        return f"{init} codigo:{self.codigo}, nombre:{self.nombre}, " \
               f"descripción:{self.descripcion}{end}"
