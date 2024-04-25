from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(
        max_length=30,
    )
    lastname = models.CharField(
        max_length=30,
    )
    age = models.PositiveSmallIntegerField(
    )
    specialization = models.CharField(
        max_length=30,
    )
    experience = models.PositiveSmallIntegerField(
    )
    image_for_doctor = models.ImageField(
        upload_to="blogs/",
        verbose_name="Фото",
    )
    creation_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.name

