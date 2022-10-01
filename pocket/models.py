from django.db import models
from user.models import *

class Pocket(models.Model):
    user_pocket = models.ForeignKey(Account, on_delete=models.RESTRICT, default='')
    pocket_name = models.CharField(primary_key=True, blank=True, max_length=50, default='Pocket')
    pocket_budget = models.BigIntegerField(default=False)
    pocket_balance = models.BigIntegerField(default=0)