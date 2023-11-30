from django.db import models

from apps.user.models import User


class Feature(models.Model):
    """
    The model for the features of the car.
    For example: an electric car, with artificial intelligence, etc.
    """

    name = models.CharField(max_length=100, verbose_name="Feature name", unique=True)
    description = models.CharField(max_length=100, verbose_name="Feature description")

    def __str__(self):
        return "Feature name: " + self.name

    class Meta:
        db_table = "Feature"


class Car(models.Model):
    """
    Car models that the user sells  on the car platform
    """

    model = models.CharField(max_length=100, verbose_name="Car model name")
    engine_power = models.PositiveSmallIntegerField(verbose_name="Car engine power")
    description = models.CharField(
        max_length=250, verbose_name="Car description", null=True
    )
    features = models.ManyToManyField(Feature, verbose_name="Car features")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Car owner")
    price = models.PositiveIntegerField(null=False, verbose_name="Car price")

    def __str__(self):
        return "Car model: " + self.model

    class Meta:
        db_table = "Car"
