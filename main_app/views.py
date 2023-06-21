from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#! Functions
#? Pawfect matches
    # if score = 3 show pet.name else append

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


def home(request):
    return render(request, 'home.html')


def gateway(request):
  return render(request, 'gateway.html')
#! Create your views here.


#? Login, render request login.html
def login(request):
    return render(request, 'gateway.html')

#? Home, render request home.html


#? user form, render request userform.html


#? pet form, render request petform.html


#? pet detail, render request pet_detail.html, id param required


#! Class based views
#? below for create, update & delete views for both pet and user
