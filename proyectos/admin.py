from django.contrib import admin
from proyectos.models import Proyecto
from proyectos.models import Participante

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Participante)