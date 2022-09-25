from django.urls import path
from .views import add_pocket

urlpatterns = [
    path('', add_pocket, name='add_pocket'),
]