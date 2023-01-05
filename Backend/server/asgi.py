import os
from channels.routing import URLRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django_asgi_application = get_asgi_application()

application=ProtocolTypeRouter(
    {
    "http": django_asgi_application
}
)
