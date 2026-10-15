from django.contrib import admin
from django.urls import include
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "api/users/",
        include("users.urls"),
    ),

    path(
        "api/cases/",
        include("cases.urls"),
    ),

    path(
        "api/patients/",
        include("patients.urls"),
    ),

    path(
        "api/consultations/",
        include("consultations.urls"),
    ),

    path(
        "api/feedback/",
        include("feedback.urls"),
    ),

]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )