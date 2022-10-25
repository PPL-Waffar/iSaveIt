from django.db import models
from user.models import Account

FEATURE_CHOICE = [
    ('payment', 'payment'),
    ('pocket', 'pocket'),
    ('transaction', 'transaction'),
    ('expense', 'expense'),
    ('financialreport', 'financialreport'),
    ('transaction', 'transaction'),
]

class Feedback(models.Model):
    user_feedback = models.ForeignKey(Account, on_delete=models.RESTRICT, default='')
    feedback_feature = models.CharField(max_length=200, choices=FEATURE_CHOICE, default='payment', null=True)
    feedback_textbox = models.TextField()
