from django.db import models

class Water_content(models.Model):
    source = models.CharField(max_length=100)
    pH = models.IntegerField()
    dissolved_oxygen = models.IntegerField()
    temperature = models.IntegerField()
    conductivity = models.IntegerField()
    turbidity = models.IntegerField()
    tds = models.IntegerField()
    chlorine = models.IntegerField()
    result = models.CharField(max_length=20)