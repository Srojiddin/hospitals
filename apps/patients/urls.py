from django.urls import path

from apps.patients.views import PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('patient/list/', PatientListView.as_view(), name='patient_list'),
    path('patient/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/delete/', PatientDeleteView.as_view(), name='patient_delete')
]