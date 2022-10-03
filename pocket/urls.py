from django.urls import path
from .views import add_pocket, delete_pocket, edit_pocket

urlpatterns = [
    path('add-pocket/', add_pocket),
    path('delete-pocket/', delete_pocket),
    path('edit-pocket/', edit_pocket),
]