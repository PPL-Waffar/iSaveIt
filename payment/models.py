from django.db import models
from pocket.models import *
PAYMENT_CHOICE = [
    ('debit card', 'debit card'),
    ('cash', 'cash'),
    ('e-wallet', 'e-wallet'),
]

# Create your models here.
class Payment(models.Model):

    pay_name = models.CharField(primary_key=True, blank=True)
    pay_amount = models.BigIntegerField(default=False)
    pay_date = models.DateTimeField(auto_now=True)
    pay_categories = models.ForeignKey(Pocket, on_delete=models.SET_DEFAULT, default='NULL')
    payment_choice = models.CharField(max_length=6, choices=PAYMENT_CHOICE, default='cash')
    
    





    