from django.urls import path
from . import views

#? URL patterns below
urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
]
