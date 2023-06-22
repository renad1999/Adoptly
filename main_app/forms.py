from django import forms
from .models import PetTable 

class PetNameForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['name']

class PetActivityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['activity_level']

class PetSociabilityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['sociability']

class PetSizeForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['size']

class PetWeightForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['weight']

class PetHealthStatusForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['healthStatus']

class PetActivityLevelForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['activity_level']

class PetVaccinationInformationForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['vaccinationInformation']

class PetMonthlyCostForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['monthlyCost']


class PetPromptsForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['prompt1', 'a1', 'prompt2', 'a2', 'prompt3', 'a3']