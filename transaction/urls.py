from django.urls import path
from .views import input_transaction

urlpatterns = [
    path('input-transaction/', input_transaction),
    
]