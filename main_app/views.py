from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import PetTable, AdoptionPreferences, UserDetails


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
      return redirect('home')
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
def home(request, pet_id=None):
    pet = PetTable.objects.get(id=pet_id)
    return render(request, 'home.html', {
      'pet': pet
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
class AdoptionPreferences(CreateView):
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