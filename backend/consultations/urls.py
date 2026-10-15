from django.urls import path

from sessions.views.create import CreateSessionView
from sessions.views.chat import ChatView
from sessions.views.complete import CompleteSessionView
from sessions.views.history import SessionHistoryView


urlpatterns = [

    path(

        "",

        CreateSessionView.as_view(),

        name="create-session",

    ),

    path(

        "<int:pk>/chat/",

        ChatView.as_view(),

        name="chat",

    ),

    path(

        "<int:pk>/complete/",

        CompleteSessionView.as_view(),

        name="complete",

    ),

    path(

        "history/",

        SessionHistoryView.as_view(),

        name="history",

    ),

]