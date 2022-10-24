from django.urls import path
from .views import add_pocket, get_pocket, delete_pocket, edit_pocket, total_pocket

urlpatterns = [
    path('add-pocket/', add_pocket),
    path('get-pocket/', get_pocket),
    path('delete-pocket/', delete_pocket),
    path('edit-pocket/', edit_pocket),
    path('total-pocket/', total_pocket),
]