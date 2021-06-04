import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import todo.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(todo.routing.websocket_urlpatterns)
    ),
})
