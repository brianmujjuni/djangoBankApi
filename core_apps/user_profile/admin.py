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

    class meta:
        model = Profile
        fields = "__all__"


class NextOfKinInLine(admin.TabularInline):
    model = NextOfKin
    extra = 1
    fields = ["first_name", "last_name", "relationship", "phone_number", "is_primary"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = [
        "user",
        "full_name",
        "phone_number",
        "email",
        "employement_status",
        "photo_preview",
    ]

    list_display_links = ["user"]
    list_filter = ["gender", "marital_status", "country","employement_status",]
    search_fields = [
        "user__first_name",
        "user__last_name",
        "user__email",
        "phone_number",
    ]
    readonly_fields = ["user"]
    fieldsets = (
        (
            _("Personal Information"),
            {
                "fields": (
                    "user",
                    "photo",
                    "id_photo",
                    "signature_photo",
                    "title",
                    "gender",
                    "date_of_birth",
                    "marital_status",
                )
            },
        ),
        (
            _("Contact Information"),
            {"fields": ("phone_number", "address", "city", "country")},
        ),
        (
            _("Identification"),
            {
                "fields": (
                    "means_of_identification",
                    "id_issue_date",
                    "id_expiry_date",
                    "passport_number",
                )
            },
        ),
        (
            _("Employment Information"),
            {
                "fields": (
                    "employement_status",
                    "employer_name",
                    "annual_income",
                    "date_of_employement",
                    "employer_address",
                    "employer_city",
                    "employer_state",
                )
            },
        ),
    )
    inlines = [NextOfKinInLine]

    def full_name(self, obj) -> str:
        return obj.user.full_name

    full_name.short_description = _("Full Name")

    def email(self, obj) -> str:
        return obj.user.email

    email.short_description = _("Email")

    def photo_preview(self, obj) -> str:
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />',
                obj.photo.url,
            )
        return _("No Photo Available")

    photo_preview.short_description = _("Photo Preview")

    @admin.register(NextOfKin)
    class NextOfKinAdmin(admin.ModelAdmin):
        list_display = [
            "full_name",
            "relationship",
            "profile",
            "is_primary",
        ]
        list_filter = ["relationship", "is_primary"]
        search_fields = [
            "first_name",
            "phone_number",
            "first_name",
            "last_name",
            "profile__user__email",
        ]

        def full_name(self, obj) -> str:
            return f"{obj.first_name} {obj.last_name}"

        full_name.short_description = _("Full Name")
