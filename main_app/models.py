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
    ('low', 'Less than an hour'),
    ('moderate', 'One to two hours'),
    ('high', 'Two hours minimum'),
)

ENERGY_LEVEL_CHOICES = (
    ('low', 'Very calm'),
    ('moderate', 'Moderate energy level'),
    ('high', 'High energy'),
)

VACCINATION_CHOICES = (
    ('N', 'No'),
    ('Y', 'Fully Vaccinated'),
)

SOCIABILITY_CHOICES = (
    ('very', 'Very sociable, loves both dogs and people'),
    ('somewhat', 'Somewhat sociable, selectively interacts'),
    ('hardly', 'Not very sociable, prefers to keep a distance'),
    ('not', 'Not sociable, avoids interaction when possible'),
)

SIZE_CHOICES = (
    ('S', 'Small, up to 9kg'),
    ('M', 'Medium, up to 27kg'),
    ('L', 'Large, up to 45kg'),
    ('XL', 'Large, over 45kg'),
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
    email = models.CharField(max_length=255,blank=True)
    username = models.CharField(max_length=255,blank=True)
    password = models.CharField(max_length=255,blank=True)
    firstName = models.CharField(max_length=255,blank=True)
    lastName = models.CharField(max_length=255,blank=True)
    phone = models.IntegerField(null=True)
    adopter = models.BooleanField(default=False,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)


#? PET TABLE MODELz
# name, species, breed, age, description charfields
# user can only choose 3 prompts, once all 3 chosen user can't add anymore
class PetTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='M')
    sociability = models.CharField(max_length=40, choices=SOCIABILITY_CHOICES, default='introvert', blank=True)
    age = models.IntegerField()
    breed = models.TextField(max_length=100) 
    size = models.CharField(
        max_length=50,
        choices=SIZE_CHOICES, default='S', blank=True
    )
    weight = models.FloatField(null=True)
    healthStatus = models.CharField(max_length=250, choices=HEALTH_STATUS_CHOICES, default='good health', blank=True)
    activity_level = models.CharField(max_length=50, choices=ACTIVITY_LEVEL_CHOICES, default='low', blank=True)
    energy_level = models.CharField(max_length=50, choices=ENERGY_LEVEL_CHOICES, default='low', blank=True)
    vaccinationInformation = models.CharField(
        max_length=1,
        choices=VACCINATION_CHOICES, default='N', blank=True
    )
    monthlyCost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, default=1.5)

    

    

#? PET PROMPTS
class Prompt(models.Model):
    prompt = models.CharField(max_length=100, choices=PROMPT_CHOICES, default='a')
    answer = models.TextField(max_length=250, null=True)
    pet = models.ForeignKey(PetTable, on_delete=models.CASCADE, related_name='prompts')


#? ADOPTION PREFERENCES
# activity levels, sociability, size, is_owner charfields
class AdoptionPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    activityLevel = models.CharField(max_length=255, choices=ACTIVITY_LEVEL_CHOICES, default='low')
    sociability = models.CharField(max_length=255, choices=SOCIABILITY_CHOICES, default='both')
    size = models.CharField( max_length=255, choices=SIZE_CHOICES, default='small')
    energyLevel = models.CharField(max_length=255, choices=ENERGY_LEVEL_CHOICES, default='low')
    liked_pets = models.ManyToManyField(PetTable, related_name='liked_by_users', blank=True)


    #? PET MATCH
# use perfect match scoring of 1 - 0 to help push perfect matches to the top of the matches list
class PetMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(PetTable, on_delete=models.CASCADE)
    matchStatus = models.BooleanField 

# #? image model
class PetImage(models.Model):
    url = models.CharField(max_length=200, null=True)
    pet= models.ForeignKey(PetTable,related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"
    
    