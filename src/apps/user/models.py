from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    """
    Registered user model
    """

    phone_regex = RegexValidator(
        regex=r"^\+1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'",
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        null=False,
        unique=True,
        verbose_name="User phone number",
    )

    def __str__(self):
        return "User name:" + self.username

    class Meta:
        db_table = "User"


class Passport(models.Model):
    """
    User passport data model. A user can only have one passport
    """

    passport_number = models.CharField(
        max_length=9, unique=True, verbose_name="User passport number"
    )
    identification_number = models.CharField(
        max_length=20, unique=True, verbose_name="User identification number"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Passport"
