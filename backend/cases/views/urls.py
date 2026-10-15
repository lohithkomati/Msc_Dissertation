from django.urls import path

from cases.views import (

    CaseListView,

    CaseDetailView,

)

urlpatterns = [

    path(

        "",

        CaseListView.as_view(),

        name="case-list",

    ),

    path(

        "<int:pk>/",

        CaseDetailView.as_view(),

        name="case-detail",

    ),

]