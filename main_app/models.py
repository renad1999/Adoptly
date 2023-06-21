from django.db import models
from django.contrib.auth.models import User

#! tuples here
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

HEALTH_STATUS_CHOICES = (
    ('good health', 'Good Health'),
    ('needs medication', 'Needs Medication'),
    ('disabled', 'Disabled'),
)

ACTIVITY_LEVEL_CHOICES = (
    ('low', 'Low'),
    ('moderate', 'Moderate'),
    ('high', 'High'),
)

VACCINATION_CHOICES = (
    ('N', 'No'),
    ('Y', 'Fully Vaccinated'),
)

SOCIABILITY_CHOICES = (
    ('introvert', 'Introvert'),
    ('extrovert', 'Extrovert'),
    ('both', 'Both'),
)

SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

#! Models go below.
#? user model
# login info
class UserDetails(models.Model):
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField()
    adopter = models.BooleanField(default=False)

#? ADOPTION PREFERENCES
# activity levels, sociability, size, is_owner charfields
class AdoptionPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activityLevel = models.CharField(max_length=50, choices=ACTIVITY_LEVEL_CHOICES)
    sociability = models.CharField(max_length=50, choices=SOCIABILITY_CHOICES)
    size = models.CharField(
        max_length=1, 
        choices=SIZE_CHOICES)


#? PET TABLE MODEL
# name, species, breed, age, description charfields
# user can only choose 3 prompts, once all 3 chosen user can't add anymore
class PetTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    sociability = models.CharField(max_length=40, choices=SOCIABILITY_CHOICES)
    age = models.IntegerField()
    breed = models.TextField(max_length=100) 
    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES
    )
    weight = models.FloatField()
    healthStatus = models.CharField(max_length=250, choices=HEALTH_STATUS_CHOICES)
    activity_level = models.CharField(max_length=50, choices=ACTIVITY_LEVEL_CHOICES)
    vaccinationInformation = models.CharField(
        max_length=1,
        choices=VACCINATION_CHOICES,
    )
    monthlyCost = models.DecimalField(max_digits=8, decimal_places=2)

    #? PET MATCH
# use perfect match scoring of 1 - 0 to help push perfect matches to the top of the matches list
class PetMatch(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_id = models.ForeignKey(PetTable, on_delete=models.CASCADE)
    matchStatus = models.CharField(max_length=50)

# #? image model
class PetImage(models.Model):
    url = models.URLField(max_length=200)
    pet_id = models.ForeignKey(PetTable, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"