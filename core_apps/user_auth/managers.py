import random 
import string
from os import getenv
from typing import Any,Optional

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def generate_username() -> str:
    bank_name = getenv("BANK_NAME")
    words = bank_name.split()
    prefix = "".join([word[0] for word in words]).upper()
    remaining_length = 12 - len(prefix) - 1
    random_chars = "".join(random.choices(string.ascii_uppercase + string.digits,k=remaining_length))
    username = f"{prefix}-{random_chars}"
    return username
