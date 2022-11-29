from django.urls import path
from .views import *

urlpatterns = [
    path('input-transaction/', input_transaction),
    path('get-transaction/', get_transaction),
    path('delete-transaction/',delete_transaction), 
    path('view-transaction/', view_all_transaction),
    
]