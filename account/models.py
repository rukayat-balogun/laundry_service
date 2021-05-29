from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_sales = models.BooleanField(default=False)
    activate = models.BooleanField(default=True)




class Category(models.Model):
    """Model definition for MODELNAME."""
    name  = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name







class Item(models.Model):
    """Model definition for Item."""
    name = models.CharField("Item Name", max_length=50)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Item."""

        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        """Unicode representation of Item."""
        return self.name



class Services(models.Model):
    """Model definition for Services."""
    item = models.ForeignKey(Item, related_name='service', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.FloatField("Item Price Per Unit", default=00.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Services."""

        verbose_name = 'Services'
        verbose_name_plural = 'Servicess'

    def __str__(self):
        """Unicode representation of Services."""
        return f'{self.item.name }  --  {self.name}'

  
