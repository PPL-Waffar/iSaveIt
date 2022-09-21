from django.db import models

# Create your models here.
class Account(models.Model):

    name = models.CharField(primary_key=True, blank=True)
    amount = models.BigIntegerField(default=False)
    date = models.DateTimeField(auto_now=True)



    