from django.db import models

# Create your models here.
from django.db import models
from users.models import User
# Create your models here.


class Item(models.Model):
    itemmanager = models.ForeignKey(
        'users.User', on_delete=models.CASCADE)
    # item categories
    VEHICLES = 'VEH'
    ELECTRONICS = 'ELE'
    FURNITURE = 'FUR'
    OTHER = 'OTH'

    ITEM_CATEGORY_CHOICES = [(VEHICLES, 'VEHICLES'), (ELECTRONICS,
                                                      'ELECTRONICS'), (FURNITURE, 'FURNITURE'), (OTHER, 'OTHER')]
    item_category = models.CharField(
        max_length=3, choices=ITEM_CATEGORY_CHOICES, blank=True)

    # item condition
    BRAND_NEW = 'BN'
    NEW = 'N'
    USED = 'U'
    NOT_WORKING = 'NW'

    ITEM_CONDITION_CHOICES = [
        (BRAND_NEW, 'BRAND NEW'), (NEW, 'NEW'), (USED, 'USED'), (NOT_WORKING, 'NOT WORKING')]

    ad_title = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='ad_img', blank=True)
    image_2 = models.ImageField(upload_to='ad_img', blank=True)
    image_3 = models.ImageField(upload_to='ad_img', blank=True)
    image_4 = models.ImageField(upload_to='ad_img', blank=True)
    image_5 = models.ImageField(upload_to='ad_img', blank=True)
    item_brand = models.CharField(max_length=25, blank=True)
    item_model = models.CharField(max_length=25, blank=True)
    item_condition = models.CharField(
        max_length=2, choices=ITEM_CONDITION_CHOICES, blank=True)
    item_description = models.TextField(max_length=5000, blank=True)
    price = models.PositiveIntegerField(blank=True)
    date_posted = models.DateTimeField(
        verbose_name="date posted", auto_now_add=True)
