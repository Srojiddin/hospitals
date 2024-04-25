# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# from apps.doctors.models import Doctor
# from apps.hospitals.models import Address
#
# class Hospital(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.OneToOneField(OtherModel, on_delete=models.CASCADE)
#     review = models.TextField(max_length=100)
#     phone_number = models.CharField(max_length=10)
#     email = models.EmailField(max_length=50)
#     image_for_hospital = models.ImageField(upload_to="blogs/", verbose_name="Фото")
#
#     def __str__(self):
#         return self.name
#
#
# class Booking(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     date_of_reservation = models.DateField(default=timezone.now)
#
#     def str(self):
#         return f"  {self.name} {self.check_in_date} {self.check_out_date} {self.date_of_reservation}"


