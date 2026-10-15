from rest_framework import generics

from patients.models import Patient

from patients.serializers import PatientListSerializer


class PatientListView(

    generics.ListAPIView

):

    serializer_class = PatientListSerializer

    queryset = Patient.objects.filter(

        active=True

    )