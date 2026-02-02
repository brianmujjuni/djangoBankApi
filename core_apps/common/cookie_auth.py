from typing import Optional,Tuple
from django.conf import settings
from django.conf import settings
from loguru import logger
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication, AuthUser
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import Token