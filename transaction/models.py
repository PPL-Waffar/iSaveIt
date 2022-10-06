from django.db import models
from pocket.models import Pocket
from user.models import *

class Transaction(models.Model):
    user_transaction = models.ForeignKey(Account, on_delete=models.RESTRICT, default='')
    transaction_payment_name = models.CharField(primary_key=True, blank=True, max_length=50)
    transaction_amount = models.BigIntegerField(default=False)
    transaction_date = models.DateField()
    transaction_type_transaction = models.CharField(max_length=50)
    transaction_type_payment = models.CharField(max_length=50)
    transaction_pocket = models.ForeignKey(Pocket, on_delete=models.RESTRICT, default='')