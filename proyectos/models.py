#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Proyecto(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre', unique=True)
    description = models.TextField(verbose_name='Descripción')
    max_participants = models.IntegerField(verbose_name='Cantidad máxima de participantes')
    status = models.CharField(max_length=1, choices=(('A','Abierto'),('C','Cerrado'),))

    def __unicode__(self):
        return self.name

class Participante(models.Model):
    proyecto = models.ForeignKey(Proyecto, blank=True, null=True)
    name = models.CharField(max_length=250, verbose_name='Nombre')
    email = models.EmailField(verbose_name='E-mail', unique=True)

    def __unicode__(self):
        return self.name