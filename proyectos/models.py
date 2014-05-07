#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Proyecto(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre', unique=True)
    description = models.TextField(verbose_name='Descripción')
    owner_name = models.TextField(verbose_name='Nombre del autor')
    technology = models.TextField(verbose_name="Tecnología/Herramienta", blank=True, null=True)
    category = models.CharField(max_length=250, verbose_name="Categoría", blank=True, null=True)
    email = models.EmailField(verbose_name="E-mail", blank=True, null=True)
    max_participants = models.IntegerField(verbose_name='Cantidad máxima de participantes')
    status = models.CharField(max_length=1, choices=(('A','Abierto'),('C','Cerrado'),))
    url = models.URLField(verbose_name="URL del repositorio", blank=True, null=True)

    def __unicode__(self):
        return self.name

class Participante(models.Model):
    proyecto = models.ForeignKey(Proyecto, blank=True, null=True)
    name = models.CharField(max_length=250, verbose_name='Nombre')
    email = models.EmailField(verbose_name='E-mail', unique=True)

    def __unicode__(self):
        return self.name