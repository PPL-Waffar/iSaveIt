from pyexpat import model
from django.db import models

class Pocket(models.Model):
    name = models.CharField(max_length=50)
    budget = model.BigIntegerField()
    

    def __str__(self):
        return self.name
