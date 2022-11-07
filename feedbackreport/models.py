from django.db import models
from user.models import Account



class Feedback(models.Model):
    user_feedback = models.ForeignKey(Account, on_delete=models.RESTRICT, default='')
    feedback_rating = models.IntegerField(default=0)
    feedback_goal = models.TextField(max_length=100, default='')
    feedback_text = models.TextField(max_length=100, default='')
    feedback_text2 = models.TextField(max_length=100, default='')
    feedback_comment = models.TextField(max_length=100, default='')
    feedback_date = models.DateField(auto_now_add=True)

