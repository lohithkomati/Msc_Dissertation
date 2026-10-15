from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cases.models import PatientCase
from sessions.models import ConsultationSession


class CreateSessionView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        case_id = request.data.get("case_id")

        if not case_id:

            return Response(
                {"detail": "case_id is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            patient_case = PatientCase.objects.get(
                pk=case_id,
                is_active=True,
            )

        except PatientCase.DoesNotExist:

            return Response(
                {"detail": "Case not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        session = ConsultationSession.objects.create(

            user=request.user,

            case=patient_case,

            messages=[],

        )

        return Response(

            {
                "id": session.id,
                "status": session.status,
                "case": patient_case.id,
            },

            status=status.HTTP_201_CREATED,

        )