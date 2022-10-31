from django.urls import path
from .views import input_transaction,get_transaction

urlpatterns = [
    path('input-transaction/', input_transaction),
    path('get-transaction/', get_transaction),
    
]