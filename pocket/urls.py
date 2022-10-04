from django.urls import path
from .views import add_pocket, get_pocket

urlpatterns = [
    path('add-pocket/', add_pocket),
    path('get-pocket/', get_pocket),
]