from django.contrib import admin
from apps.programa.models import Programa, AsignacionBeneficio, TipoAsistencia
# Register your models here.

admin.site.register(Programa)
admin.site.register(AsignacionBeneficio)
admin.site.register(TipoAsistencia)
