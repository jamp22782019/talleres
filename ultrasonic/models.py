from django.db import models
import uuid

class Ultrasonic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    latitud = models.IntegerField(verbose_name='Latitud')
    longitud = models.IntegerField(verbose_name='Longitud')
    area = models.IntegerField(verbose_name='Area')



    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)