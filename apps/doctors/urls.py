from django.urls import path

from apps.doctors.views import DoctorListView,DoctorDetailView,DoctorUpdateView,DoctorDeleteView

urlpatterns = [
    path('doctor/list/', DoctorListView.as_view(), name='doctor.html'),
    path('doctor/detail/', DoctorDetailView.as_view(), name='department.html'),
    path('doctor/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor/delete/', DoctorDeleteView.as_view(), name='doctor_delete')
]