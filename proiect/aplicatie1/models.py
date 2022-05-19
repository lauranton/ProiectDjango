from django.db import models

# Create your models here.
class Cursuri(models.Model):
    NumeCurs = models.CharField(max_length=100)
    ProfCurs = models.CharField(max_length=100)
    DescriereCurs = models.CharField(max_length=300)
    activ = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.NumeCurs} - {self.ProfCurs} -{self.DescriereCurs}"

