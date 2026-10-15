from rest_framework import generics

from patients.models import Patient

from patients.serializers import PatientSerializer


class PatientDetailView(

    generics.RetrieveAPIView

):

    serializer_class = PatientSerializer

    queryset = Patient.objects.filter(

        active=True

    )