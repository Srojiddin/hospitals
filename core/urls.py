from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/',include('apps.doctors.urls')),
    path('patients/',include('apps.patients.urls')),
    path('users/',include('apps.users.urls')),
    path('hospitals/',include('apps.hospitals.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
