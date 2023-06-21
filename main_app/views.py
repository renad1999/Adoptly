from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

#! Functions
#? Pawfect matches
    # if score = 3 show pet.name else append


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
