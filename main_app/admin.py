from django.contrib import admin
from .models import PetTable, AdoptionPreferences

# Register your models here.
admin.site.register(PetTable)
admin.site.register(AdoptionPreferences)