from django.views import generic
from apps.patients.models import Patient
from apps.patients.forms import PatientCreateForm, PatientUpdateForm, PatientDeleteForm


class PatientListView(generic.ListView):
    model = Patient
    template_name = 'patients.html'
    context_object_name = 'patients'


class PatientCreateView(generic.CreateView):
    model = Patient
    form_class = PatientCreateForm
    template_name = 'patient_create.html'
    success_url = ('index.html')


class PatientUpdateView(generic.UpdateView):
    model = Patient
    form_class = PatientUpdateForm
    template_name = 'patient_update.html'


class PatientDetailsView(generic.DetailView):
    model = Patient
    template_name = 'patient_details.html'


class PatientDeleteView(generic.DeleteView):
    model = Patient
    form_class = PatientDeleteForm
    template_name = 'patient_delete.html'
