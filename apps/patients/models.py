from django.db import models
from django.utils import timezone
from apps.doctors.models import Doctor


class Patient(models.Model):
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    age = models.PositiveSmallIntegerField(
    )
    disease = models.CharField(
        max_length=120,
    )
    choosing_a_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name="vyberite vashego vracha",
        related_name="patients"
    )
    creation_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.first_name
