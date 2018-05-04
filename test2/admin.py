from django.contrib import admin
from test2.models import *

# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	pass
