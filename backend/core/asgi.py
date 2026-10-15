import os

from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "core.settings.local",
)

django_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_application,

        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    # websocket routes added later
                ]
            )
        ),
    }
)