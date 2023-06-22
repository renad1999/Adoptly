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

PROMPT_CHOICES = [
    ('a', 'If your pet had a catchphrase, what would it be?'),
    ('b', "What's the funniest thing your pet has ever done?"),
    ('c', "If your pet was a character from a movie or book, who would they be and why?"),
    ('d', "Can you describe a time when your pet was surprisingly clever?"),
    ('e', "What's your pet's favorite 'toy' that isn't actually a toy?"),
    ('f', "How does your pet act when they want your attention?"),
    ('g', "How does your pet show they're happy?"),
    ('h', "If your pet could talk for 60 seconds, what do you think they would say?"),
    ('i', "How would your pet react to seeing their reflection in the mirror?"),
    ('j', "What activity does your pet love so much that they'd do it for hours"),
    ('k', "If your pet could have a superpower, based on their personality, what would it be?"),
    ('l', "What's the most peculiar habit your pet has?"),
    ('m', "How does your pet act when they meet new people or animals?"),
    ('n', "If your pet had a job, based on their personality, what would it be?"),
    ('o', "What song would be your pet's personal theme song?"),
    ('p', "What human food does your pet beg for the most?"),
    ('q', "Can you describe a situation in which your pet acted bravely?"),
    ('r', "How would your pet react if they saw a squirrel in the backyard?"),
    ('s', "What's the most unusual friendship your pet has struck up with another animal?"),
    ('t', "If your pet could choose a vacation destination, where would it be?"),
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
    url = models.URLField(max_length=200)
    pet_id = models.ForeignKey(PetTable, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"