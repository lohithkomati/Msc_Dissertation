from django.db import models


class Patient(models.Model):

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    GENDER_CHOICES = [

        (MALE, "Male"),

        (FEMALE, "Female"),

        (OTHER, "Other"),

    ]

    patient_id = models.CharField(

        max_length=30,

        unique=True,

    )

    full_name = models.CharField(

        max_length=150,

    )

    age = models.PositiveIntegerField()

    gender = models.CharField(

        max_length=20,

        choices=GENDER_CHOICES,

    )

    occupation = models.CharField(

        max_length=120,

        blank=True,

    )

    condition = models.CharField(

        max_length=200,

    )

    personality = models.TextField()

    background_story = models.TextField()

    opening_statement = models.TextField()

    avatar = models.ImageField(

        upload_to="patients/",

        blank=True,

        null=True,

    )

    active = models.BooleanField(

        default=True,

    )

    created_at = models.DateTimeField(

        auto_now_add=True,

    )

    updated_at = models.DateTimeField(

        auto_now=True,

    )

    class Meta:

        ordering = [

            "full_name",

        ]

    def __str__(self):

        return f"{self.full_name} ({self.condition})"