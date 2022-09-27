from django.urls import path
from .views import add_pocket, delete_pocket, edit_pocket

urlpatterns = [
    path('', add_pocket, name='add_pocket'),
    path('delete/', delete_pocket, name='delete_pocket'),
    path('edit/', edit_pocket, name='edit_pocket'),
]