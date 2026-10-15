from django.db import models

from sessions.models import ConsultationSession


class FeedbackReport(models.Model):

    session = models.OneToOneField(
        ConsultationSession,
        on_delete=models.CASCADE,
        related_name="feedback_report",
    )

    overall_score = models.PositiveIntegerField(
        default=0
    )

    domain_scores = models.JSONField(
        default=dict
    )

    missed_questions = models.JSONField(
        default=list
    )

    diagnosis_correct = models.BooleanField(
        default=False
    )

    diagnosis_feedback = models.TextField(
        blank=True
    )

    narrative_feedback = models.TextField(
        blank=True
    )

    keyword_checks = models.JSONField(
        default=dict
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [

            "-generated_at",

        ]

    def __str__(self):

        return f"Feedback {self.session_id}"