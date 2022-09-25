from django.db import models
from pocket.models import *
PAYMENT_CHOICE = [
    ('debit card', 'debit card'),
    ('cash', 'cash'),
    ('e-wallet', 'e-wallet'),
]

# Create your models here.
class Payment(models.Model):

    pay_name = models.CharField(primary_key=True, blank=True, max_length=250)
    pay_amount = models.BigIntegerField(default=False)
    pay_date = models.DateTimeField(auto_now=True)
    pay_categories = models.ForeignKey(Pocket, on_delete=models.SET_DEFAULT, default='NULL',null=True)
    payment_choice = models.CharField(max_length=200, choices=PAYMENT_CHOICE, default='cash',null=True)
    
    





    