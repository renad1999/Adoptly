from django.contrib import admin
from .models import PetTable, AdoptionPreferences, PetImage, UserDetails, PetMatch, Prompt

# Register your models here.
admin.site.register(PetTable)
admin.site.register(AdoptionPreferences)
admin.site.register(PetImage)
admin.site.register(UserDetails)
admin.site.register(Prompt)
admin.site.register(PetMatch)