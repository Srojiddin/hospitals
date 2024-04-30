from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.doctors.models import Doctor
from django.conf import settings


# class Hospital(models.Model):
#     hospital_choice = (
#         ('Доктор Ислам'),
#         ('Клиника Касиет'),
#         ('Доктор Айдаров'),
#     )

class Appointment (models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    choosing_a_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name="vyberite vashego vracha",
    )
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    date_of_reservation = models.DateField(
        default=timezone.now,
    )

    def str(self):
        return f" {self.user} {self.check_in_date} {self.check_out_date} {self.date_of_reservation}"