from django.db import models

NEWS_CHOICE = [
    ('tips', 'tips'),
    ('news', 'news'),
]

class Newsletter(models.Model):
    newsletter_text = models.TextField(max_length=10000, default='')
    newsletter_picture = models.ImageField(upload_to='newsletter/pictures/', default='')
    newsletter_category = models.CharField(max_length=10, choices=NEWS_CHOICE, default='tips')
