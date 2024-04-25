from django import forms
from apps.patients.models import Patient


class PatientBaseForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'age', 'disease', 'choosing_a_doctor', 'creation_date']


class PatientCreateForm(PatientBaseForm):
    pass


class PatientUpdateForm(PatientBaseForm):
    pass


class PatientDeleteForm(PatientBaseForm):
    pass


class PatientDetailsForm(PatientBaseForm):
    pass

