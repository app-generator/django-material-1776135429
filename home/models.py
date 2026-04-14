# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    barcode = models.TextField(max_length=255, null=True, blank=True)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True, blank=True)
    low_stock_threshold = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Role(models.Model):

    #__Role_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Role_FIELDS__END

    class Meta:
        verbose_name        = _("Role")
        verbose_name_plural = _("Role")


class Type(models.Model):

    #__Type_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Type_FIELDS__END

    class Meta:
        verbose_name        = _("Type")
        verbose_name_plural = _("Type")


class Inventory_Transaction(models.Model):

    #__Inventory_Transaction_FIELDS__
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Inventory_Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Inventory_Transaction")
        verbose_name_plural = _("Inventory_Transaction")


class Productprice(models.Model):

    #__Productprice_FIELDS__
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_out = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Productprice_FIELDS__END

    class Meta:
        verbose_name        = _("Productprice")
        verbose_name_plural = _("Productprice")


class Owner(models.Model):

    #__Owner_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    #__Owner_FIELDS__END

    class Meta:
        verbose_name        = _("Owner")
        verbose_name_plural = _("Owner")


class Location(models.Model):

    #__Location_FIELDS__
    address = models.TextField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    #__Location_FIELDS__END

    class Meta:
        verbose_name        = _("Location")
        verbose_name_plural = _("Location")


class Productbatch(models.Model):

    #__Productbatch_FIELDS__
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    expiry_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    received_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    #__Productbatch_FIELDS__END

    class Meta:
        verbose_name        = _("Productbatch")
        verbose_name_plural = _("Productbatch")



#__MODELS__END
