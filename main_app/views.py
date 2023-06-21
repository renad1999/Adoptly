from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import PetTable, AdoptionPreferences


#! Functions
#? Pawfect matches
    # if score = 3 show pet.name else append

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
def home(request):
    return render(request, 'home.html')


#? pet details, render request pets/details.html
def pet_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  return render(request, 'pets/details.html', {
    'pet': pet
  })



#! Class based views
#? below for create, update & delete views for both pet and user

#will we need an if statement for the boolean value of if the user is
#creating an adopter account or 
class AdoptionPreferences(CreateView):
  model = AdoptionPreferences
  fields ='__all__'

class PetCreate(CreateView):
  model = PetTable
  fields ='__all__'