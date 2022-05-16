import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string
from core import managers as core_managers


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MAIL = "male"
    GENDER_FEMAIL = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MAIL, "Male"),
        (GENDER_FEMAIL, "Female"),
        (GENDER_OTHER, "Other"),
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
        (CURRENCY_KRW, "KRW"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOIES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUATGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOIES, default=LOGIN_EMAIL)
    objects = core_managers.CustomUserManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string("emails/verify_email.html", {"secret": secret})
            send_mail(
                "Verify Airbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.username],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
