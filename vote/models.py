#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=250, verbose_name="Nombre de candidato")
	votes = models.IntegerField(verbose_name="Cantidad de votos")

	def __unicode__(self):
		return self.name + str(self.votes)
