# from django.urls import re_path
# from django_test.drawing_project.drawing_app import consumers
#
# websocket_urlpatterns = [
#     re_path(r'ws/drawing/$', consumers.DrawingConsumer.as_asgi()),
# ]

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from channels.auth import AuthMiddlewareStack

from . import consumers
from django.core.asgi import get_asgi_application


# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     path("ws/drawing_board/<str:room_name>/", consumers.DrawingBoardConsumer.as_asgi()),
#                 ]
#             )
#         ),
#     }
# )
websocket_urlpatterns = [
    re_path(r"ws/drawing_board/(?P<room_name>\w+)/$", consumers.DrawingBoardConsumer.as_asgi()),
]