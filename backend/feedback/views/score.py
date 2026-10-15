from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework.views import APIView

from sessions.models import ConsultationSession

from feedback.models import FeedbackReport

from services.feedback.scorer import generate_feedback


class GenerateFeedbackView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    async def post(self, request, session_id):

        try:

            session = ConsultationSession.objects.get(

                pk=session_id,

                user=request.user,

            )

        except ConsultationSession.DoesNotExist:

            return Response(

                {

                    "detail":

                    "Session not found."

                },

                status=status.HTTP_404_NOT_FOUND,

            )

        result = await generate_feedback(

            session

        )

        report, _ = FeedbackReport.objects.update_or_create(

            session=session,

            defaults={

                "overall_score":
                    result["overall_score"],

                "domain_scores":
                    result["domain_scores"],

                "missed_questions":
                    result["missed_questions"],

                "diagnosis_correct":
                    result["diagnosis_correct"],

                "diagnosis_feedback":
                    result["diagnosis_feedback"],

                "narrative_feedback":
                    result["narrative_feedback"],

                "keyword_checks":
                    result["keyword_checks"],

            }

        )

        return Response(

            {

                "id": report.id,

                "overall_score":
                    report.overall_score,

            },

            status=status.HTTP_200_OK,

        )