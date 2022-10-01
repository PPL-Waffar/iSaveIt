from django.urls import path
from payment.views import flutter_add_payment
urlpatterns = [
     path('flu-add-payment/', flutter_add_payment),
]