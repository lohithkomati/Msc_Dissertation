from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from sessions.models import ConsultationSession

from services.patient import build_system_prompt
from services.llm import llm_complete
from services.tts import synthesise


class ChatView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    async def post(self, request, pk):

        try:

            session = ConsultationSession.objects.get(

                pk=pk,

                user=request.user,

            )

        except ConsultationSession.DoesNotExist:

            return Response(

                {

                    "detail": "Session not found."

                },

                status=status.HTTP_404_NOT_FOUND,

            )

        user_message = request.data.get(

            "message",

            "",

        )

        history = request.data.get(

            "history",

            [],

        )

        case = request.data.get(

            "case",

            {},

        )

        prompt = build_system_prompt(

            case

        )

        history.append(

            {

                "role": "user",

                "content": user_message,

            }

        )

        answer = await llm_complete(

            messages=history,

            system_prompt=prompt,

            temperature=0.35,

            max_tokens=250,

        )

        history.append(

            {

                "role": "assistant",

                "content": answer,

            }

        )

        session.messages = history

        session.save()

        audio = synthesise(answer)

        return Response(

            {

                "response": answer,

                "audio_b64": audio,

            }

        )