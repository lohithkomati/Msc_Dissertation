from rest_framework import serializers

from .models import PatientCase


class PatientCaseSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = PatientCase

        fields = "__all__"


class PatientCaseListSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = PatientCase

        fields = [

            "id",

            "title",

            "patient_name",

            "condition",

            "difficulty",

            "specialty",

        ]