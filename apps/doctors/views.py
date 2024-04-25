from django.views import generic

from apps.doctors.models import Doctor
from apps.doctors.forms import DoctorCreateForm, DoctorUpdateForm, DoctorDeleteForm


class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DoctorCreateForm()
        return context


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'


class DoctorUpdateView(generic.UpdateView):
    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'doctor_update.html'
    success_url = '/index.html'


class DoctorDeleteView(generic.DeleteView):
    model = Doctor
    form_class = DoctorDeleteForm
    template_name = 'doctor_delete.html'
    context_object_name = 'object'
    success_url = '/index.html'
