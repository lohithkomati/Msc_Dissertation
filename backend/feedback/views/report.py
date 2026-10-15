from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework.views import APIView

from feedback.models import FeedbackReport

from feedback.serializers import FeedbackSerializer


class FeedbackReportView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    def get(self, request, session_id):

        try:

            report = FeedbackReport.objects.get(

                session_id=session_id,

                session__user=request.user,

            )

        except FeedbackReport.DoesNotExist:

            return Response(

                {

                    "detail":

                    "Feedback not found."

                },

                status=status.HTTP_404_NOT_FOUND,

            )

        serializer = FeedbackSerializer(

            report

        )

        return Response(

            serializer.data

        )