from django.urls import path
from payment.views import flutter_add_payment, flutter_delete_payment, flutter_get_payment, flutter_update_payment
urlpatterns = [
     path('flu-add-payment/', flutter_add_payment),
     path('flu-get-payment/', flutter_get_payment),
     path('flu-update-payment/', flutter_update_payment),
     path('flu-delete-payment/', flutter_delete_payment),
]