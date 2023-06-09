from django.db import models

from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from django.utils import timezone


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, default=False)
    description = models.TextField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, default=False)
    description = models.TextField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.price * self.quantity
        super().save(*args, **kwargs)


