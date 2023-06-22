from django import forms
from .models import PetTable, Prompt

class PetBasicInfoForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['name', 'gender', 'sociability', 'age', 'breed', 'size', 'weight', 
                  'healthStatus', 'activity_level', 'vaccinationInformation', 'monthlyCost']

class PetPromptsForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['prompt1', 'a1', 'prompt2', 'a2', 'prompt3', 'a3']