from __future__ import unicode_literals
from django.db import  models


class Proizvod(models.Model):

    ime_proizvoda=models.CharField(max_length=200)
    kategorija_proizvoda=models.CharField(max_length=200)
    def __str__(self):
        return  self.ime_proizvoda