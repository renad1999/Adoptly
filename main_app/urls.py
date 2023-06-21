from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


#? URL patterns below
urlpatterns = [
    path('', views.gateway, name='gateway'), 
    path('home/', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]


#TODO NOTE TO RENAD AND KYLE: The gateway page has links to sign up and login pages. The sign up and login pages currently redirect to 'Home' page, but the sign up page should redirect to the questionnaire when that's created and the login page should redirect to the matches page (the A page in the wireframes). 