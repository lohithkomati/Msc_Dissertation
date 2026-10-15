from rest_framework import generics

from cases.models import PatientCase

from cases.serializers import (

    PatientCaseListSerializer,

)


class CaseListView(

    generics.ListAPIView

):

    serializer_class = (

        PatientCaseListSerializer

    )

    queryset = (

        PatientCase.objects.filter(

            is_active=True

        )

    )