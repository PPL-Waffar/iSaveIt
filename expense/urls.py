from django.urls import path
from .views import add_expense, total_expense, view_expense,get_expense

urlpatterns = [
     path('view-expense/', view_expense),
     path('add-expense/', add_expense),
     path('total-expense/', total_expense),
     path('get-expense/', get_expense),
]