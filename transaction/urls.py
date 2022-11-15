from django.urls import path
from .views import input_transaction, get_transaction,view_all_transaction

urlpatterns = [
    path('input-transaction/', input_transaction),
    path('get-transaction/', get_transaction),
    path('view-transaction/', view_all_transaction),
    
]