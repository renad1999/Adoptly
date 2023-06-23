from django import forms
from .models import PetTable, PetImage

class PetNameForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['name']
        labels = {
            'name': 'What is your pet\'s name?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'my-input-class'}), 
        }


class PetActivityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['activity_level']
        labels = {
            'activity_level': 'How much does your dog like being walked?',
        }
        widgets = {
            'activity_level': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

class PetSociabilityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['sociability']
        labels = {
            'sociability': 'How social is your pet?',
        }
        widgets = {
            'sociability': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

class PetSizeForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['size']
        labels = {
            'size': 'What size is your pet?',
        }
        widgets = {
            'size': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

class PetAgeForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['age']
        labels = {
            'age': 'How old is your pet?',
        }


class PetWeightForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['weight']
        labels = {
            'wight': 'What weight is your pet?',
        }

class PetHealthStatusForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['healthStatus']
        labels = {
            'healthStatus': 'How would you describe your pet\'s health?',
        }
        widgets = {
            'healthStatus': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

class PetEnergyLevelForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['energy_level']
        labels = {
            'energy_level': 'How would you describe your pet\'s energy levels?',
        }
        widgets = {
            'energy_level': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

class PetVaccinationInformationForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['vaccinationInformation']
        labels = {
            'vaccinationInformation': 'Is your pet vaccinated?',
        }
        widgets = {
            'vaccinationInformation': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

class PetMonthlyCostForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['monthlyCost']
        labels = {
            'monthlyCost': 'What do you spend on average each month on essentials for your pet? Think food, vet bills, grooming, etc. £',
        }


class PetPromptsForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['prompt1', 'a1', 'prompt2', 'a2', 'prompt3', 'a3']
        labels = {
            'prompt1': 'Written Prompts',
            'prompt2': 'Written Prompts',
            'prompt3': 'Written Prompts',
        }
       

class PetImageForm(forms.ModelForm):
    photo1 = forms.ImageField(label='+')
    photo2 = forms.ImageField(label='+', required=False)
    photo3 = forms.ImageField(label='+', required=False)

    class Meta:
        model = PetImage
        fields = ['photo1', 'photo2', 'photo3']
        labels = {
            'photo1':'+', 
            'photo2':'+',
            'photo3':'+',
        }