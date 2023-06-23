from django import forms
<<<<<<< HEAD
from .models import PetTable, PetImage
=======
from .models import AdoptionPreferences
from .models import PetTable
   

class AdoptionPreferencesActivity(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['activityLevel']


        
class AdoptionPreferencesSociability(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['sociability']

        
class AdoptionPreferencesEnergy(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['energyLevel']

        
class AdoptionPreferencesSize(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['size']         
        
        
class UserChoiceForm(forms.ModelForm):
    BOOL_CHOICES = [(True, 'Yes'), (False, 'No')]  
    is_owner = forms.BooleanField(
        widget = forms.RadioSelect (choices=BOOL_CHOICES),
        required= False
    )     
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb

class PetNameForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['name']
        labels = {
            'name': 'What is your pet\'s name?',
        }
<<<<<<< HEAD
        widgets = {
            'name': forms.TextInput(attrs={'class': 'my-input-class'}), 
        }
    
    def __init__(self, *args, **kwargs):
        super(PetNameForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['name'].widget.attrs['id'] = 'pet_name'

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'name_q'


=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
class PetActivityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['activity_level']
        labels = {
            'activity_level': 'How much does your dog like being walked?',
        }
<<<<<<< HEAD
        widgets = {
            'activity_level': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

    def __init__(self, *args, **kwargs):
        super(PetActivityForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['activity_level'].widget.attrs['id'] = 'pet_name'

        # all fields on form
        for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'name_q'


=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
class PetSociabilityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['sociability']
        labels = {
            'sociability': 'How social is your pet?',
        }
<<<<<<< HEAD
        widgets = {
            'sociability': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

    def __init__(self, *args, **kwargs):
        super(PetSociabilityForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['sociability'].widget.attrs['id'] = 'pet_name'

        # all fields on form
        for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'name_q'

=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
class PetSizeForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['size']
        labels = {
            'size': 'What size is your pet?',
        }
<<<<<<< HEAD
        widgets = {
            'size': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
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
<<<<<<< HEAD
        }
        widgets = {
            'healthStatus': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
        }
class PetEnergyLevelForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['energy_level']
        labels = {
            'energy_level': 'How would you describe your pet\'s energy levels?',
        }
<<<<<<< HEAD
        widgets = {
            'energy_level': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
class PetVaccinationInformationForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['vaccinationInformation']
        labels = {
            'vaccinationInformation': 'Is your pet vaccinated?',
        }
<<<<<<< HEAD
        widgets = {
            'vaccinationInformation': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }

=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
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
<<<<<<< HEAD
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
=======










>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
