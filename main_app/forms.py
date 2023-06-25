from django import forms
from .models import PetTable, PetImage

from .models import AdoptionPreferences
from .models import PetTable
   

class AdoptionPreferencesActivity(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['activityLevel']
        labels = {
            'activityLevel': 'Preferred activity level for your desired pet',
        }
        widgets = {
            'activityLevel': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AdoptionPreferencesActivity, self).__init__(*args, **kwargs)

        # specific field
        self.fields['activityLevel'].widget.attrs['id'] = 'desired_activity_level'

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'activity_level_q'



class AdoptionPreferencesSociability(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['sociability']
        labels = {
            'sociability': 'Preferred sociability for your desired pet',
        }
        widgets = {
            'sociability': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AdoptionPreferencesSociability, self).__init__(*args, **kwargs)

        # specific field
        self.fields['sociability'].widget.attrs['id'] = 'desired_sociability'

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'sociability_q'


        
class AdoptionPreferencesEnergy(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['energyLevel']
        labels = {
            'energyLevel': 'Preferred energy level for your desired pet',
        }
        widgets = {
            'energyLevel': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AdoptionPreferencesEnergy, self).__init__(*args, **kwargs)

        # specific field
        self.fields['energyLevel'].widget.attrs['id'] = 'desired_energy_level'

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'energy_level_q'


        
class AdoptionPreferencesSize(forms.ModelForm):
    class Meta:
        model = AdoptionPreferences
        fields = ['size']
        labels = {
            'size': 'Preferred pet size',
        }
        widgets = {
            'size': forms.RadioSelect(attrs={'class': 'pet-create-radio'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AdoptionPreferencesSize, self).__init__(*args, **kwargs)

        # specific field
        self.fields['size'].widget.attrs['id'] = 'desired_pet_size'

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'size_q'

        

class UserChoiceForm(forms.ModelForm):
    BOOL_CHOICES = [(True, 'Yes'), (False, 'No')]  
    is_owner = forms.BooleanField(
        widget = forms.RadioSelect (choices=BOOL_CHOICES),
        required= False
    )     




class PetNameForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['name']
        label = {
            'name': 'What is your pet\'s name?',
        }
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


class PetActivityForm(forms.ModelForm):
    # title = 'How much does your dog like being walked?'
    class Meta:
        model = PetTable
        fields = ['activity_level']
        label = {
            'activity_level': 'How much does your dog like being walked?',
        }
        widgets = {
            'activity_level': forms.RadioSelect(attrs={'class': 'my-input-class'}), 
        }

    def __init__(self, *args, **kwargs):
        # self.title = kwargs.pop('title', '')
        super(PetActivityForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['activity_level'].widget.attrs['id'] = 'pet_name'

        # all fields on form
        for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'name_q'
                self.fields[field].widget.attrs['id'] = 'activity'

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

    def __init__(self, *args, **kwargs):
        super(PetSociabilityForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['sociability'].widget.attrs['id'] = 'pet_name'
        

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'name_q'
            self.fields[field].widget.attrs['id'] = 'sociability'

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
    def __init__(self, *args, **kwargs):
        super(PetSizeForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['size'].widget.attrs['id'] = 'pet_name'
        

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'name_q'
            self.fields[field].widget.attrs['id'] = 'size'

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
            'weight': 'What weight is your pet?',
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
    def __init__(self, *args, **kwargs):
        super(PetEnergyLevelForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['energy_level'].widget.attrs['id'] = 'pet_name'
        

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'name_q'
            self.fields[field].widget.attrs['id'] = 'energy_level'

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
    
    def __init__(self, *args, **kwargs):
        super(PetVaccinationInformationForm, self).__init__(*args, **kwargs)

        # specific field
        self.fields['vaccinationInformation'].widget.attrs['id'] = 'pet_name'
        

        # all fields on form
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'name_q'
            self.fields[field].widget.attrs['id'] = 'vaccinationInformation'

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
            'prompt1': 'First Prompt',
            'prompt2': 'Second Prompt',
            'prompt3': 'Third Prompt',
            'a1': '',
            'a2': '',
            'a3': '',
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
