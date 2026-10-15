from django.urls import path

from feedback.views import (

    GenerateFeedbackView,

    FeedbackReportView,

)

urlpatterns = [

    path(

        "<int:session_id>/",

        FeedbackReportView.as_view(),

        name="feedback-report",

    ),

    path(

        "<int:session_id>/generate/",

        GenerateFeedbackView.as_view(),

        name="feedback-generate",

    ),

]