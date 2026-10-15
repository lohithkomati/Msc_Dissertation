from django.utils import timezone

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from sessions.models import ConsultationSession


class CompleteSessionView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    def post(self, request, pk):

        session = ConsultationSession.objects.get(

            pk=pk,

            user=request.user,

        )

        session.status = ConsultationSession.COMPLETED

        session.completed_at = timezone.now()

        transcript = []

        for message in session.messages:

            speaker = (

                "Doctor"

                if message["role"] == "user"

                else "Patient"

            )

            transcript.append(

                f"{speaker}: {message['content']}"

            )

        session.transcript = "\n".join(

            transcript

        )

        session.save()

        return Response(

            {

                "status": "completed"

            }

        )