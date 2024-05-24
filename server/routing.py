from django.urls import re_path
from . import rpc_controller

websocket_urlpatterns = [
    re_path(r'ws/msflistener/', rpc_controller.RPC_Socket.as_asgi()),
]