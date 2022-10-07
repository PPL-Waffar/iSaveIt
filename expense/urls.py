from django.urls import path
from .views import view_expense

urlpatterns = [
     path('view-expense/', view_expense),
]