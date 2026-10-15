from rest_framework import serializers

from .models import ConsultationSession


class SessionSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = ConsultationSession

        fields = "__all__"


class SessionCreateSerializer(

    serializers.Serializer

):

    case_id = serializers.IntegerField()