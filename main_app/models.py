from django.db import models
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage


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

ENERGY_LEVEL_CHOICES = (
    ('low', 'Very Energetic'),
    ('moderate', 'Medium'),
    ('high', 'Chill'),
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

PROMPT_CHOICES = [
    ('a', 'My catchphrase is'),
    ('b', "My most embarrassing moment"),
    ('c', "If I was a character from a movie or a book, I would be"),
    ('d', "A time when I was surprisingly clever "),
    ('e', "My favorite 'toy' that isn't actually a toy"),
    ('f', "When I want my human's attention I"),
    ('g', "I show I'm happy by"),
    ('h', "If I could talk for 60 seconds I would say"),
    ('i', "When I see my reflection in the mirror I"),
    ('j', "An activity I could do for hours is"),
    ('k', "My superpower would be"),
    ('l', "My weirdest habit is"),
    ('m', "When I meet new people or dogs I"),
    ('n', "If I had a human job it would be"),
    ('o', "My theme song would be"),
    ('p', "I salivate over"),
    ('q', "I was really brave when"),
    ('r', "When I see a squirrel I"),
    ('s', "I had an unusual friendship with"),
    ('t', "My dream day"),
    # Add more prompts here...
]

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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    sociability = models.CharField(max_length=40, choices=SOCIABILITY_CHOICES, default='introvert')
    age = models.IntegerField()
    breed = models.TextField(max_length=100) 
    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES, default='S'
    )
    weight = models.FloatField()
    healthStatus = models.CharField(max_length=250, choices=HEALTH_STATUS_CHOICES, default='good health')
    activity_level = models.CharField(max_length=50, choices=ACTIVITY_LEVEL_CHOICES, default='low')
    energy_level = models.CharField(max_length=50, choices=ENERGY_LEVEL_CHOICES, default='low')
    vaccinationInformation = models.CharField(
        max_length=1,
        choices=VACCINATION_CHOICES, default='N'
    )
    monthlyCost = models.DecimalField(max_digits=8, decimal_places=2)
    prompt1 = models.CharField(max_length=100, choices=PROMPT_CHOICES, null=True)
    a1 = models.TextField(max_length=250, null=True)
    prompt2 = models.CharField(max_length=100, choices=PROMPT_CHOICES, null=True)
    a2 = models.TextField(max_length=250, null=True)
    prompt3 = models.CharField(max_length=100, choices=PROMPT_CHOICES, null=True)
    a3 = models.TextField(max_length=250, null=True)

    #? PET MATCH
# use perfect match scoring of 1 - 0 to help push perfect matches to the top of the matches list
class PetMatch(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_id = models.ForeignKey(PetTable, on_delete=models.CASCADE)
    matchStatus = models.CharField(max_length=50)

# #? image model
class PetImage(models.Model):
    photo = models.ImageField(upload_to='pets/', storage=S3Boto3Storage(), null=True)
    url = models.CharField(max_length=200, null=True)
    pet_id = models.ForeignKey(PetTable, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"