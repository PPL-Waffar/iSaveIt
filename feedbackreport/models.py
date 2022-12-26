from django.db import models
from user.models import Account



class Feedback(models.Model):
    user_feedback = models.ForeignKey(Account, on_delete=models.RESTRICT, default='')
    customer_ID = models.AutoField(primary_key=True, editable=False)
    feedback_rating = models.IntegerField(default=0)
    feedback_goal = models.TextField(max_length=100, default='')
    feedback_text = models.TextField(max_length=100, default='')
    feedback_text2 = models.TextField(max_length=100, default='')
    feedback_comment = models.TextField(max_length=100, default='')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    

