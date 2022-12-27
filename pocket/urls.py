from django.urls import path
from .views import add_pocket, get_pocket, delete_pocket, edit_pocket,all_balance,all_expense

urlpatterns = [
    path('add-pocket/', add_pocket),
    path('get-pocket/', get_pocket),
    path('delete-pocket/', delete_pocket),
    path('edit-pocket/', edit_pocket),
    path('all-balance/', all_balance),
    path('all-expense/', all_expense),
]