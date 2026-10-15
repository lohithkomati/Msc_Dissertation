from django.conf import settings
from django.db import models

from cases.models import PatientCase


class ConsultationSession(models.Model):

    ACTIVE = "active"
    COMPLETED = "completed"
    ABANDONED = "abandoned"

    STATUS_CHOICES = [

        (ACTIVE, "Active"),
        (COMPLETED, "Completed"),
        (ABANDONED, "Abandoned"),

    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="consultations",
    )

    case = models.ForeignKey(
        PatientCase,
        on_delete=models.CASCADE,
        related_name="consultations",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )

    started_at = models.DateTimeField(
        auto_now_add=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    duration_seconds = models.PositiveIntegerField(
        default=0,
    )

    messages = models.JSONField(
        default=list,
    )

    transcript = models.TextField(
        blank=True,
    )

    overall_score = models.FloatField(
        default=0,
    )

    feedback = models.JSONField(
        default=dict,
    )

    class Meta:

        ordering = [

            "-started_at",

        ]

    def __str__(self):

        return f"Session {self.pk}"