from django.db import models

class Pocket(models.Model):
    name = models.CharField(max_length=50)
    budget = models.BigIntegerField()
    user_pocket = models.ForeignKey(Account,on_delete=models.RESTRICT,default ='')

    def __str__(self):
        return self.name
