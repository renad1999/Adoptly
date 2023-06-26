import logging
import boto3
import uuid
import os
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import PetTable, AdoptionPreferences, UserDetails, Prompt, PetImage
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from .forms import PromptForm, InlinePromptFormset, AdoptionPreferencesActivity, AdoptionPreferencesSize, AdoptionPreferencesSociability, AdoptionPreferencesEnergy, PetNameForm, PetActivityForm, PetSociabilityForm, PetSizeForm,PetHealthStatusForm, PetEnergyLevelForm, PetVaccinationInformationForm, PetMonthlyCostForm, PetAgeForm, UserForm

#! Forms

PETFORMS = [
    ("name", PetNameForm),
    ("age", PetAgeForm),
    ("activity", PetActivityForm),
    ("sociability", PetSociabilityForm),
    ("size", PetSizeForm),
    ("health", PetHealthStatusForm),
    ("energy", PetEnergyLevelForm),
    ("vaccination", PetVaccinationInformationForm),
    ("cost", PetMonthlyCostForm)
]

FORMS = [ ("activityLevel", AdoptionPreferencesActivity),
    ("size", AdoptionPreferencesSize),
    ("sociability", AdoptionPreferencesSociability),
     ("energyLevel", AdoptionPreferencesEnergy), ]
    #  ("Are you a pet owner?", )]

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
       matches.append((pet, score)) #Append the pet and its score as a tuple
    sorted_matches = sorted(matches, key=lambda x: x[1], reverse=True) #Sort by score in a descending order
    sorted_pets = [pet for pet, score in sorted_matches] #Extract sorted pets
  return render(request, 'home.html', {'pets': sorted_pets})


#? Login and signup, render request gateway.html
def signup(request): #! Sign up function
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
      return redirect('redirect_form')
    
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def gateway(request):
  return render(request, 'gateway.html')

def add_photo(request, pet_id):
    pet = PetTable.objects.get(id=pet_id)    # photo-file will be the "name" attribute on the <input type="file">
    if pet.images.count() >= 3:
        return HttpResponse('You cannot upload more than 3 images')
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            print(url)
            # we can assign to cat_id or cat (if you have a cat object)
            PetImage.objects.create(url=url, pet=pet)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('pet_update', pk=pet_id)
 
def delete_photo(request, pet_id, photo_id):
    pet = PetTable.objects.get(id=pet_id)
    try:
        photo = PetImage.objects.get(id=photo_id)
    except PetImage.DoesNotExist:
        return redirect('pet_update', pk=pet_id)  # redirect if photo doesn't exist
    photo.delete()
    return redirect('pet_update', pk=pet_id)

def pet_update(request, pet_id):
    pet = PetTable.objects.get(id=pet_id)

    # calculate the number of placeholders needed
    num_images = pet.images.all().count()
    num_placeholders = max(0, 3 - num_images)

    print(f'Number of images: {num_images}')
    print(f'Number of placeholders: {num_placeholders}')

    context = {
        'pet': pet,
        'num_placeholders': range(num_placeholders),
    }
    return render(request, 'PetUpdate_form.html', context)
   
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
  return redirect('home', user_id=user_id)

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
  fields =['activityLevel', 'sociability', 'size']

class AdoptionPreferencesUpdate(UpdateView):
  model = AdoptionPreferences
  fields =['activityLevel', 'sociability', 'size']

class AdoptionPreferencesDelete(DeleteView):
  model = AdoptionPreferences
  success_url ='/'

#? pet forms
class PetCreate(CreateView):
  model = PetTable
  fields ='__all__'
  template_name = 'main_app/PetTable_form.html' 
  
  def form_valid(self, form):
    self.object = form.save(commit=False)  # Create the object but don't save to the database yet
    self.object.user = self.request.user  # Set the user
    self.object.save()  # Now save the object
    return HttpResponseRedirect(reverse('pet_update', args=[self.object.id]))  # Redirect to PetUpdate view

class PetUpdate(UpdateView):
    model = PetTable
    fields = ['sociability', 'size', 'healthStatus', 'activity_level', 'vaccinationInformation', 'monthlyCost']
    template_name = 'main_app/PetUpdate_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = self.object
        if self.request.POST:
            context['prompt_formset'] = InlinePromptFormset(self.request.POST, instance=self.object)
        else:
            context['prompt_formset'] = InlinePromptFormset(instance=self.object, prefix='prompt_formset')
        return context

    def form_valid(self, form):
      print(self.request.POST)
      context = self.get_context_data()
      prompt_formset = context['prompt_formset']
      self.object = form.save()
      print(form.errors)

      if prompt_formset.is_valid():
          prompt_formset.instance = self.object
          prompt_formset.save()
      else:
          print(prompt_formset.errors)

      return HttpResponseRedirect(self.get_success_url())
        # returning HttpResponseRedirect to the success url directly    
    def get_success_url(self):
        return reverse('pet_details', args=[self.object.id])
    
class PromptUpdate(UpdateView):
    model = Prompt
    fields = ['prompt', 'response']
    template_name = 'main_app/PromptUpdate_form.html'
    
    def get_success_url(self):
        return reverse('pet_details', args=[self.object.id])

  
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
          return HttpResponseRedirect(reverse('home'))


class PetCreateWizard(SessionWizardView):
    form_list = PETFORMS
    template_name = 'main_app/PetTable_form.html'

    def get_form(self, step=None, data=None, files=None):
        form = super().get_form(step, data, files)
        print(f"Serving form: {type(form).__name__}")
        print(f"Form fields:  {form.fields}")
        print(f"Form is valid: {form.is_valid()}")
        print(f"Form errors: {form.errors}")
        print(f"Form cleaned data: {form.cleaned_data if form.is_valid() else None}")
        print(f"Current Step: {self.steps.current}")
        return form

    def done(self, form_list, **kwargs):
        instance = PetTable()

        # Check if user is authenticated
        if self.request.user.is_authenticated:
            instance.user = self.request.user
            for form in form_list:
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)
            
            instance.save()
            return HttpResponseRedirect(reverse('pet_update', kwargs={'pk': instance.id}))
        else:
            # redirect to login page, or some other response, if user is not authenticated
            return HttpResponseRedirect(reverse('login'))

    def get_form_step_data(self, form):
        data = super().get_form_step_data(form)
        return data


class PetNameCreate(CreateView):
    model = PetTable
    form_class = PetNameForm
    template_name = 'pets/PetTable_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)  # Create the object but don't save to the database yet
        self.object.user = self.request.user  # Set the user
        self.object.save()  # Now save the object
        self.request.session['new_pet_id'] = self.object.id  # Save the id to the session
        return HttpResponseRedirect(self.get_success_url())  # Redirect to the next part of the form

    def get_success_url(self):
        return reverse('pet_update')


class AdoptionPreferencesCreateView(CreateView):
    model = AdoptionPreferences
    form_class = AdoptionPreferencesForm
    template_name = 'main_app/adoptionpreferences_form.html'
    success_url = '/home'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('')
    
def preferences_complete(request):
    return render(request, '')

def pet_guidance(request):
    return render(request, 'pet_guidance.html')


def success_stories(request):
    return render(request, 'success_stories.html')

def help_center(request):
    return render(request, 'help_center.html')

def messages(request):
    return render(request, 'messages.html')



def redirect_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.user = request.user
            user_details.save()
            if user_details.adopter == True:
                return redirect('user_create')
            else:
                return redirect('pet_create')
    else:
        form = UserForm()
    
    return render(request, 'redirect_form.html')
