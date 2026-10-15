from django.urls import path

from patients.views import (

    PatientListView,

    PatientDetailView,

)

urlpatterns = [

    path(

        "",

        PatientListView.as_view(),

        name="patient-list",

    ),

    path(

        "<int:pk>/",

        PatientDetailView.as_view(),

        name="patient-detail",

    ),

]