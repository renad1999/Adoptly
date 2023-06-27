#! NOTE to KYLE and RENAD. Please install : pip install faker, requests

import requests
from faker import Faker
from random import choice
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import PetTable, Prompt, PetImage
from ...models import GENDER_CHOICES, HEALTH_STATUS_CHOICES, ACTIVITY_LEVEL_CHOICES, ENERGY_LEVEL_CHOICES, VACCINATION_CHOICES, SOCIABILITY_CHOICES, SIZE_CHOICES, PROMPT_CHOICES

class Command(BaseCommand):
    help = 'Create random dogs'

    def handle(self, *args, **options):
        # Deleting existing pets.
        PetTable.objects.all().delete()

        fake = Faker()
        user = User.objects.first()  # Using first user for simplicity

        for _ in range(100):
            pet = PetTable(
                user=user,
                name=fake.first_name(),  # Generates only first name
                gender=choice(GENDER_CHOICES)[0],
                sociability=choice(SOCIABILITY_CHOICES)[0],
                age=fake.random_int(min=1, max=10),
                breed=fake.word(),
                size=choice(SIZE_CHOICES)[0],
                weight=fake.random_int(min=1, max=100),
                healthStatus=choice(HEALTH_STATUS_CHOICES)[0],
                activity_level=choice(ACTIVITY_LEVEL_CHOICES)[0],
                energy_level=choice(ENERGY_LEVEL_CHOICES)[0],
                vaccinationInformation=choice(VACCINATION_CHOICES)[0],
                monthlyCost=fake.random_int(min=50, max=500)
            )
            pet.save()

            # Saving 3 images for each pet
            for _ in range(3):
                response = requests.get('https://dog.ceo/api/breeds/image/random')
                image_url = response.json()['message']

                pet_image = PetImage(
                    url=image_url,
                    pet=pet
                )
                pet_image.save()

            for i in range(3):
                prompt = Prompt(
                    prompt=choice(PROMPT_CHOICES)[0],
                    answer=fake.sentence(),
                    pet=pet
                )
                prompt.save()
