from django.db import models

class Pocket(models.Model):
    pocket_name = models.CharField(max_length=50)
    pocket_budget = models.BigIntegerField()
    balance = models.BigIntegerField(default=0)
    

    def __str__(self):
        return self.pocket_name
