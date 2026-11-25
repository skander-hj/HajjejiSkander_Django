from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils import timezone


def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError(
            "La date de naissance doit être antérieure à aujourd’hui."
        )


phone_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="Le téléphone doit contenir 8 chiffres."
)


class User(AbstractUser):
    pass


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(User):
    license_number = models.CharField(
        max_length=6, unique=True,
        validators=[MinLengthValidator(6)]
    )

    phone = models.CharField(
        max_length=8, validators=[phone_validator]
    )

    specialties = models.ManyToManyField(Specialty)
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

class Patient(User):
    national_id = models.CharField(
        max_length=8, unique=True,
        validators=[RegexValidator(
            r"^\d{8}$", message="La CIN doit contenir 8 chiffres."
        )]
    )

    phone = models.CharField(
        max_length=8, validators=[phone_validator]
    )

    birth_date = models.DateField(
        validators=[validate_past_date]
    )
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'