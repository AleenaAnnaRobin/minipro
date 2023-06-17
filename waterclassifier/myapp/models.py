from django.db import models
from django.contrib.auth.models import User

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

class Register(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="register_user")

    
    