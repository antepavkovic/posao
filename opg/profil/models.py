from __future__ import unicode_literals
from django.db import  models


class Profil(models.Model):

    name=models.CharField(max_length=200,default="-")
    surname=models.CharField(max_length=200,default="-")
    opg_name=models.CharField(max_length=200,default="-")
    adress=models.CharField(max_length=200,default="-")
    tele=models.IntegerField(default="5")


    def __str__(self):
        return  self.name