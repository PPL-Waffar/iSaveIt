from django.db import models

NEWS_CHOICE = [
    ('tips', 'tips'),
    ('news', 'news'),
]

class Newsletter(models.Model):
    newsletter_title = models.TextField(max_length=100, default='')
    newsletter_text = models.TextField(max_length=10000, default='')
    newsletter_picture = models.ImageField(upload_to='newsletter/pictures/', blank=True, null=True)
    newsletter_category = models.CharField(max_length=10, choices=NEWS_CHOICE, default='tips')
