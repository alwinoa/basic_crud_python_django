from django.db import models

# Create your models here.
class CreateMovie(models.Model):
    tittle=models.CharField(max_length=25)
    year=models.DateField(null=False)
    summary=models.TextField(max_length=25)
