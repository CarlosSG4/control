from django.contrib import admin
from .models import Doctors, Consultorios

# Register your models here.

admin.site.register(Doctors)
admin.site.register(Consultorios)