from django.db import models
from django.core.exceptions import ValidationError

class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150)
    documento = models.CharField(max_length=50)  # alfanumérico
    correo_electronico = models.EmailField()
    fecha_asistencia = models.DateField()
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    presente = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha_asistencia', 'hora_ingreso']

    def __str__(self):
        return f"{self.nombre_completo} — {self.fecha_asistencia}"

    def clean(self):
        # validación a nivel de modelo: hora_salida no puede ser antes que hora_ingreso
        if self.hora_ingreso and self.hora_salida and self.hora_salida < self.hora_ingreso:
            raise ValidationError({'hora_salida': 'La hora de salida no puede ser anterior a la hora de ingreso.'})
