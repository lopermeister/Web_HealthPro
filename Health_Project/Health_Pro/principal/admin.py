from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pacientes)
admin.site.register(Doctores)
admin.site.register(Medicamentos)
admin.site.register(Clinicas)
admin.site.register(Consultorios)
admin.site.register(Medicamentos_Pacientes)
admin.site.register(Doctores_Consultorios)
admin.site.register(Citas)
