from django import forms
from .models import AdoptionPreferences
   
#    BOOL_CHOICES = [(True, 'Yes'), (False, 'No')]
#    is_pet_owner = forms.BooleanField (
#       widget=forms.RadioSelect(choices=BOOL_CHOICES),
#       required=False
#    


class AdoptionPreferencesActivity(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['activityLevel']


        
class AdoptionPreferencesSociability(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['sociability']

        
class AdoptionPreferencesSize(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['size']         
        
        
        
        
