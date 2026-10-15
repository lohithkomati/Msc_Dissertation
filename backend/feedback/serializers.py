from rest_framework import serializers

from .models import FeedbackReport


class FeedbackSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = FeedbackReport

        fields = "__all__"