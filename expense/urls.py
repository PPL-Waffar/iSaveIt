from django.urls import path
from .views import add_expense, view_expense

urlpatterns = [
     path('view-expense/', view_expense),
     path('add-expense/', add_expense),
]