from django.contrib import admin

from .models import PatientCase


@admin.register(PatientCase)
class PatientCaseAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "patient_name",

        "condition",

        "specialty",

        "difficulty",

        "is_active",

    )

    list_filter = (

        "difficulty",

        "specialty",

        "is_active",

    )

    search_fields = (

        "title",

        "condition",

        "patient_name",

    )