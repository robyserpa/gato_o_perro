from django.contrib import admin
from apiSNN.models import Libro
from apiSNN.models import Persona
from apiSNN.models import Image
# from apiSNN.models import Resultados
# Register your models here.
admin.site.register(Libro)
admin.site.register(Persona)
admin.site.register(Image)
# admin.site.register(Resultados)