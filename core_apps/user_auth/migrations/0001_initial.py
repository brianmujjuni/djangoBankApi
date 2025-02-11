# Generated by Django 4.2.15 on 2025-02-11 23:04

import core_apps.user_auth.managers
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=12, unique=True, verbose_name="Username"
                    ),
                ),
                (
                    "security_question",
                    models.CharField(
                        choices=[
                            ("maiden_name", "What is your mother's maiden name?"),
                            ("favorite_color", "What is your favorite color?"),
                            ("birth_city", "What is the city where you were born?"),
                            (
                                "childhood_friend",
                                "What is the name of your childhood best friend?",
                            ),
                        ],
                        max_length=30,
                        verbose_name="Security Question",
                    ),
                ),
                (
                    "security_answer",
                    models.CharField(max_length=30, verbose_name="Security Answer"),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=30, verbose_name="First Name"),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Middle Name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=30, verbose_name="Last Name"),
                ),
                (
                    "id_no",
                    models.PositiveIntegerField(unique=True, verbose_name="ID Number"),
                ),
                (
                    "account_status",
                    models.CharField(
                        choices=[("active", "Active"), ("locked", "Locked")],
                        default="active",
                        max_length=10,
                        verbose_name="Account Status",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("customer", "Customer"),
                            ("account_executive", "Account Executive"),
                            ("teller", "Teller"),
                            ("branch_manager", "Branch Manager"),
                        ],
                        default="customer",
                        max_length=20,
                        verbose_name="Role",
                    ),
                ),
                ("failed_login_attempts", models.PositiveSmallIntegerField(default=0)),
                ("last_failed_login", models.DateTimeField(blank=True, null=True)),
                ("otp", models.CharField(blank=True, max_length=6, verbose_name="OTP")),
                (
                    "otp_expiry_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="OTP Expiry Time"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ["-date_joined"],
            },
            managers=[
                ("objects", core_apps.user_auth.managers.UserManager()),
            ],
        ),
    ]
