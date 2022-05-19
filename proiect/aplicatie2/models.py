from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Profesori(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=150)
    Profcurs = models.CharField(max_length=50)
    activ = models.BooleanField(default=True)



    def __str__(self):
        return f"{self.nume} - {self.prenume} - {self.Profcurs}"
