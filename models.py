from django.db import models

# Create your models here.
class build(models.Model):
    name=models.CharField(max_length=20, blank=False, null=False, primary_key=True)
    password=models.CharField()
    mail=models.EmailField(null=False)
    phone=models.ImageField(null=False, blank=True)
