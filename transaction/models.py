from django.db import models
from pocket.models import Pocket
from payment.models import Payment
from user.models import Account

TRANSACTION_TYPE = [
    ('Expense', 'Expense'),
    ('Income', 'Income'),
]

class Transaction(models.Model):
    user_transaction = models.ForeignKey(Account, on_delete=models.RESTRICT, default='')
    transaction_payment_name = models.CharField(primary_key=True, blank=True, max_length=200)
    transaction_amount = models.BigIntegerField(default=False)
    transaction_date = models.DateField()
    transaction_transaction_type = models.CharField(max_length=200, choices=TRANSACTION_TYPE, default='Expense',null=True)
    transaction_payment_type = models.ForeignKey(Payment, on_delete=models.SET_DEFAULT, default='NULL',null=True)
    transaction_pocket = models.ForeignKey(Pocket, on_delete=models.SET_DEFAULT, default='NULL',null=True)