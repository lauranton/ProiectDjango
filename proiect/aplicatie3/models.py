from django.db import models

# Create your models here.
class Studenti(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    specializare = models.CharField(max_length=50)
    grupa = models.CharField(max_length=10)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nume} - {self.prenume} - {self.specializare} - {self.grupa}"


