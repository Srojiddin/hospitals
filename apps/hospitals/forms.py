from django import forms
from apps.hospitals.models import Appointment


class AppointmentCreateFrom(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['__all__']


class AppointmentDetailForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['__all__']