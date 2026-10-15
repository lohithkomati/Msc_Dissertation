from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (

        "patient_id",

        "full_name",

        "condition",

        "age",

        "gender",

        "active",

    )

    search_fields = (

        "patient_id",

        "full_name",

        "condition",

    )

    list_filter = (

        "gender",

        "active",

    )