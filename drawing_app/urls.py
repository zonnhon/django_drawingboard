# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('<str:room_name>/', views.drawing_board, name='drawing_board'),
]