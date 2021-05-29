from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from account.models import *





class CustomerProfile(models.Model):
    user = models.OneToOneField(User, related_name='customeruser', on_delete=models.CASCADE)
    phone_number = models.CharField("Customer Phone Number", max_length=11)
    address = models.CharField("Customer Address", max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CustomerProfile"
        verbose_name_plural = "CustomerProfiles"

    def __str__(self):
        return f'{self.user.name} - {self.phone_number}'
""" 
    def get_absolute_url(self):
        return reverse("CustomerProfile_detail", kwargs={"pk": self.pk}) """


