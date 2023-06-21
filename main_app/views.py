from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import PetTable, UserDetails





#! Functions
#? Pawfect matches
    # if score = 3 show pet.name else append
def find_matches(request):
  user_id = request.session['user_id']
  user = UserDetails.objects.get(id=user_id)
  pets = PetTable.objects.all()
  matches = []
  for pet in pets:
    score = 0
    if user.activity_level == pet.activity_level:
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
def home(request):
    return render(request, 'home.html')


#? pet details, render request pets/details.html
def pet_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  return render(request, 'pets/details.html', {
    'pet': pet
  })

#? pet form, render request petform.html


#? pet detail, render request pet_detail.html, id param required


#! Class based views
#? below for create, update & delete views for both pet and user

#will we need an if statement for the boolean value of if the user is
#creating an adopter account or 
class UserCreate(CreateView):
  model = unk
  fields ='__all__'

class PetCreate(CreateView):
  model = unk
  fields ='__all__'