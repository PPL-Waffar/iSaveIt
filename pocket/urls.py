from django.urls import path
from .views import add_pocket

urlpatterns = [
    path('add-pocket/', add_pocket),
]