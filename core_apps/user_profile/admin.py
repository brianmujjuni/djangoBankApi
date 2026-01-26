from django.contrib import admin
from cloudinary.forms import CloudinaryFileField
from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import Profile, NextOfKin

# Register your models here.
class ProfileAdminForm(forms.ModelForm):
    photo = CloudinaryFileField(
        options={
            "crop": "thumb",
            "width": 200,
            "height": 200,
            "folder": "bank_photos",
        },
        required=False,
    )