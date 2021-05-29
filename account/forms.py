from customer.models import CustomerProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import *


class SalesSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_sales = True
        if commit:
            user.save()
        return user


class CustomerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=11)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        phone_number = self.cleaned_data.get('phone_number')
        CustomerProfile.objects.create(user=user, phone_number=phone_number)
        return user