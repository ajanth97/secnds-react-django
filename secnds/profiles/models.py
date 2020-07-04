from django.db import models
from users.models import User
# Create your models here.


class Profile(models.Model):
    profilemanager = models.OneToOneField(
        'users.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50)
# province_choices
    WESTERN = 'WP'
    CENTRAL = 'CP'
    SOUTHERN = 'SP'
    NORTH_WESTERN = 'NW'
    SABARAGAMUWA = 'SG'
    EASTERN = 'EP'
    NORTH_CENTRAL = 'NC'
    UVA = 'UP'
    NORTHERN = 'NP'

    PROVINCE_CHOICES = [(WESTERN, 'Western'), (CENTRAL, 'Central'), (SOUTHERN, 'Southern'), (NORTH_WESTERN, 'North Western'), (
        SABARAGAMUWA, 'Sabaragamuwa'), (EASTERN, 'Eastern'), (NORTH_CENTRAL, 'North Central'), (UVA, 'Uva'), (NORTHERN, 'Northern')]

    province_choices = models.CharField(max_length=2, choices=PROVINCE_CHOICES)

    mobile_number = models.CharField(max_length=10)
