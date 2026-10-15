from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (

        (
            "Academic Information",

            {

                "fields": (

                    "role",

                    "university",

                    "programme",

                    "year",

                    "avatar",

                    "bio",

                    "email_verified",

                    "consultation_count",

                    "average_score",

                )

            },

        ),

    )

    list_display = (

        "username",

        "email",

        "role",

        "consultation_count",

        "average_score",

        "is_staff",

    )

    list_filter = (

        "role",

        "is_staff",

        "is_superuser",

    )