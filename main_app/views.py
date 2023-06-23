
import boto3
import uuid
import os
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from .models import PetTable, AdoptionPreferences, UserDetails, PetImage
=======
from .models import PetTable, AdoptionPreferences, UserDetails
from .forms import AdoptionPreferencesActivity, AdoptionPreferencesSize, AdoptionPreferencesSociability, AdoptionPreferencesEnergy, UserChoiceForm
from formtools.wizard.views import SessionWizardView
FORMS = [ ("activityLevel", AdoptionPreferencesActivity),
    ("size", AdoptionPreferencesSize),
    ("sociability", AdoptionPreferencesSociability),
     ("energyLevel", AdoptionPreferencesEnergy),
     ("Are you a pet owner?", UserChoiceForm)]



>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PetNameForm, PetActivityForm, PetSociabilityForm, PetSizeForm, PetWeightForm,PetHealthStatusForm, PetEnergyLevelForm, PetVaccinationInformationForm, PetMonthlyCostForm, PetAgeForm, PetImageForm, PetPromptsForm, PetImageForm


<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
#! Forms

PETFORMS = [("name", PetNameForm), 
         ("Age", PetAgeForm),
         ("activity", PetActivityForm),
         ("sociability", PetSociabilityForm),
         ("size", PetSizeForm),
         ("weight", PetWeightForm),
         ("healthStatus", PetHealthStatusForm),
         ("activity_level", PetEnergyLevelForm),
         ("vaccinationInformation", PetVaccinationInformationForm),
         ("monthlyCost", PetMonthlyCostForm),
         ("prompts", PetPromptsForm),
         ("image", PetImageForm)
]
<<<<<<< HEAD
>>>>>>> development
=======
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb

#! Functions
#? Pawfect matches
    # if score = 3 show pet.name else append
def find_matches(request):
  user_id = request.session['user_id']
  user = AdoptionPreferences.objects.get(id=user_id)
  pets = PetTable.objects.all()
  matches = []
  for pet in pets:
    score = 0
    if user.activityLevel == pet.activity_level:
        score += 1
    if user.sociability == pet.sociability:
        score += 1
    if user.size == pet.size:
       score += 1
       
    if score >= 2:
       matches.append(pet)
  return render(request, 'matches.html', {'matches': matches})


#? Login and signup, render request gateway.html
def signup(request): #! Sign up function, do not touch! - Lou
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('user_create')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



def gateway(request):
  return render(request, 'gateway.html')
#! Create your views here.


#? Home, render request home.html
def home(request):
    # pet = PetTable.objects.get(id=pet_id)
    pets = PetTable.objects.all()
    return render(request, 'home.html', {
      'pets': pets
    })


#? pet details, render request pets/details.html
def pet_detail(request, pet_id):
  pet = PetTable.objects.get(id=pet_id)
  return render(request, 'pets/details.html', {
    'pet': pet
  })


#? Profile settings
def user_settings(request):
  return render(request, 'profile_settings.html')


#? Pet matches (list of pets already matched with)
def matches(request):
  return render(request, 'matches.html')

#? About page
def about(request):
  return render(request, 'about.html')


#? Matching func 
def assoc_pet(request, user_id, pet_id):
  UserDetails.objects.get(id=user_id).PetTable.add(pet_id)
  return redirect(home, user_id=user_id)

#? Unmatching func
def unassoc_pet(request, user_id, pet_id):
  UserDetails.objects.get(id=user_id).PetTable.remove(pet_id)
  return redirect('home', user_id=user_id)

#! Class based views
#? below for create, update & delete views for both pet and user

#? adoption preference forms
#will we need an if statement for the boolean value of if the user is
#creating an adopter account or pet account? - KB
class AdoptionPreferencesForm(CreateView):
  model = AdoptionPreferences
  fields ='__all__'

class AdoptionPreferencesUpdate(UpdateView):
  model = AdoptionPreferences
  fields ='__all__'

class AdoptionPreferencesDelete(DeleteView):
  model = AdoptionPreferences
  success_url ='/'

#? pet forms
class PetCreate(CreateView):
  model = PetTable
  fields ='__all__'

class PetUpdate(UpdateView):
  model = PetTable
  # Chosen these as the only editable options to update a pet - KB
  fields =['sociability', 'size', 'healthStatus', 'activity_level', 'vaccinationInformation', 'monthlyCost', 
           'prompt1', 'a1', 'prompt2', 'a2', 'prompt3', 'a3']
  
class PetDelete(DeleteView):
  model = PetTable
  # maybe need a 'are you sure you wish to delete' or a form option
  # 'why are you deleting, has  {% pet.name %}  found a new home?' - KB
  success_url ='/'


  # questionnare 
class AdoptionPreferencesWizard(SessionWizardView):
  form_list =  FORMS
  template_name = 'main_app/adoptionpreferences_form.html'

  def done(self, form_list, **kwargs):
    instance = AdoptionPreferences()
    instance.user=self.request.user
    for form in form_list:
      for field, value in form.cleaned_data.items():
          setattr(instance, field, value)
          instance.save()
          return HttpResponseRedirect(reverse(''))



# class PetCreateWizard(SessionWizardView):
#     form_list = PETFORMS
#     template_name = 'main_app/pettable_form.html'

#     def get_form(self, step=None, data=None, files=None):
#         form = super(PetCreateWizard, self).get_form(step, data, files)

#         # add form for photo upload if it's the last step
#         if step == '3':
#             form = PetImageForm(data, files)
#         return form

#     def done(self, form_list, **kwargs):
#       instance = PetTable()
#       instance.user = self.request.user
#       for form in form_list:
#         for field, value in form.cleaned_data.items():
#             setattr(instance, field, value)
#       instance.save()
#       return HttpResponseRedirect(reverse('home'))
    

class PetCreateWizard(SessionWizardView):
    form_list = PETFORMS
    template_name = 'main_app/pettable_form.html'

    def get_form(self, step=None, data=None, files=None):
        form = super(PetCreateWizard, self).get_form(step, data, files)
        print(f"Serving form: {type(form).__name__}")

        print("Form fields: ", form.fields)

        if form is None:
          form = PetImageForm(data, files)  # if super call fails, at least return an empty PetImageForm
        elif isinstance(form, PetImageForm):
          form = PetImageForm(data, files)  # if it's a PetImageForm, create a new instance with the provided data and files

        print(f"Serving form: {type(form).__name__}")
        return form

    def done(self, form_list, **kwargs):
<<<<<<< HEAD
        instance = PetTable()
        instance.user = self.request.user
        for form in form_list:
          if not isinstance(form, PetImageForm):
            for field, value in form.cleaned_data.items():
                setattr(instance, field, value)
        instance.save()  # save the instance first before creating PetImage

        for form in form_list:
            if isinstance(form, PetImageForm):
                for i in range(1, 4):  # iterate over the three photos
                    photo_file = form.cleaned_data.get(f'photo{i}')

                    if photo_file:
                        s3 = boto3.client('s3')
                        # need a unique "key" for S3 / needs image file extension too
                        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                        try:
                            bucket = os.environ['S3_BUCKET']
                            s3.upload_fileobj(photo_file, bucket, key)
                            # build the full url string
                            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                            # create PetImage instance for each file
                            PetImage.objects.create(photo=photo_file, url=url, pet_id=instance)
                        except Exception as e:
                            print('An error occurred uploading file to S3')
                            print(e)
            else:
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)

        instance.save()
        return HttpResponseRedirect(reverse('home'))

=======
      instance = PetTable()
      instance.user = self.request.user
      for form in form_list:
        for field, value in form.cleaned_data.items():
            setattr(instance, field, value)
      instance.save()
      return HttpResponseRedirect(reverse(''))
>>>>>>> a375687f06f76c2a254b4946854d2ce21eb7a5bb
    
    def get_form_step_data(self, form):
        data = super().get_form_step_data(form)

        # If form is an instance of PetImageForm then append files data as well
        if isinstance(form, PetImageForm):
            data.update(self.get_form_step_files(form))
        return data

class PetNameCreate(CreateView):
  model = PetTable
  form_class = PetNameForm
  template_name = 'pets/PetTable_form.html' 

  def form_valid(self, form):
      self.object = form.save(commit=False)  # Create the object but don't save to the database yet
      self.object.user = self.request.user  # Set the user
      self.object.save()  # Now you can save the object
      self.request.session['new_pet_id'] = self.object.id  # Save the id to the session
      return HttpResponseRedirect(self.get_success_url())  # Redirect to the next part of the form

  def get_success_url(self):
      return reverse('home')  
  
  

class AdoptionPreferencesCreateView(CreateView):
    model = AdoptionPreferences
    form_class = AdoptionPreferencesForm
    template_name = 'main_app/adoptionpreferences_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('')
    

def preferences_complete(request):
    return render(request, '')
