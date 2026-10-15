from django.contrib.auth.password_validation import validate_password

from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework.views import APIView


class ChangePasswordView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    def post(self, request):

        old_password = request.data.get(

            "old_password"

        )

        new_password = request.data.get(

            "new_password"

        )

        if not request.user.check_password(

            old_password

        ):

            return Response(

                {

                    "detail":

                    "Old password incorrect."

                },

                status=status.HTTP_400_BAD_REQUEST,

            )

        validate_password(

            new_password,

            request.user,

        )

        request.user.set_password(

            new_password

        )

        request.user.save()

        return Response(

            {

                "detail":

                "Password updated."

            }

        )