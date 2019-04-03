from django.contrib import admin
from .models import perfiles
from .models import Especialidades, Agendar_cita
from .models import Doctors, Consultorios


admin.site.register(perfiles)
admin.site.register(Especialidades)
admin.site.register(Doctors)
admin.site.register(Consultorios)
admin.site.register(Agendar_cita)