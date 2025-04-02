from django.db import models
import random

def generate_accountnumber():
    return random.randint(000000000000,999999999999)

def generate_cifnumber():
    return random.randint(000000000000,999999999999)

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    aadhar_card = models.CharField(max_length=12, unique=True)
    city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12, unique=True)
    account_number = models.BigIntegerField(unique=True, default = generate_accountnumber)
    cif_number = models.BigIntegerField(unique=True, default = generate_cifnumber)

    def __str__(self):
        return self.name

