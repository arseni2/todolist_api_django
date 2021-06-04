from django.urls import path
from .consumers import TodoAddConsumer

websocket_urlpatterns = [
    path('todo/<str:text>/', TodoAddConsumer.as_asgi()),
]