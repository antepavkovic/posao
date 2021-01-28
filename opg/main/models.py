from __future__ import unicode_literals
from django.db import  models


class Main(models.Model):

    ime=models.CharField(max_length=200,default="-")
    prezime=models.CharField(max_length=200,default="-")
    naziv_opga=models.CharField(max_length=200,default="-")
    adresa=models.CharField(max_length=200,default="-")
    telefon=models.IntegerField(default="5")
    email=models.CharField(max_length=200,default="-")
    potvrda_emaila=models.CharField(max_length=200,default="-")
    lozinka=models.CharField(max_length=200,default="-")

    def __str__(self):
        return  self.ime