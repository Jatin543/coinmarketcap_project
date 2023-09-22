from django.urls import path
from . import views

urlpatterns = [
    path('receive_data/', views.receive_data, name='receive_data'),
    path('get_latest_data/', views.get_latest_data, name='get_latest_data'),
]

