from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MAIL = "male"
    GENDER_FEMAIL = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MAIL, "Male"),
        (GENDER_FEMAIL, "Female"),
        (GENDER_OTHER, "Other")
    )

    LANGUAGE_ENGLISH = "en"
    LANGUATGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUATGE_KOREAN, "Korean"),
    )

    CURRNECY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICE = (
        (CURRNECY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUATGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
