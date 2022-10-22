from django.urls import path
from .views import add_expense, total_expense, view_expense

urlpatterns = [
     path('view-expense/', view_expense),
     path('add-expense/', add_expense),
     path('total-expense/', total_expense),
]