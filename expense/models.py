from django.db import models
from payment.models import PAYMENT_CHOICE
from pocket.models import Pocket
from user.models import Account

EXPENSE_TYPE = [
    ('Lend Money', 'Lend Money'),
    ('Debt', 'Debt'),
]

PAYMENT_CHOICE = [
    ('debit card', 'debit card'),
    ('cash', 'cash'),
    ('e-wallet', 'e-wallet'),
]

class Expense(models.Model):
    user_expense = models.ForeignKey(Account,on_delete=models.RESTRICT,default ='')
    expense_name = models.CharField(max_length = 50)
    expense_amount = models.BigIntegerField(default=False)
    expense_date = models.DateField()
    expense_type = models.CharField(max_length=200, choices=EXPENSE_TYPE, default='Lend Money',null=True)
    expense_person = models.CharField(max_length = 50)
    expense_payment_choice = models.CharField(max_length=200, choices=PAYMENT_CHOICE, default='cash',null=True)
    expense_pocket = models.ForeignKey(Pocket, on_delete=models.SET_DEFAULT, default='NULL',null=True)