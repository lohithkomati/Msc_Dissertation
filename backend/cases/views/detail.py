from rest_framework import generics

from cases.models import PatientCase

from cases.serializers import (

    PatientCaseSerializer,

)


class CaseDetailView(

    generics.RetrieveAPIView

):

    serializer_class = (

        PatientCaseSerializer

    )

    queryset = (

        PatientCase.objects.filter(

            is_active=True

        )

    )