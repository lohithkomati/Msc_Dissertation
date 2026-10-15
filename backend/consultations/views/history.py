from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from sessions.models import ConsultationSession
from sessions.serializers import SessionSerializer


class SessionHistoryView(

    generics.ListAPIView

):

    permission_classes = [

        IsAuthenticated

    ]

    serializer_class = SessionSerializer

    def get_queryset(self):

        return ConsultationSession.objects.filter(

            user=self.request.user

        ).order_by(

            "-started_at"

        )