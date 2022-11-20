from django.db import models

NEWS_CHOICE = [
    ('tips', 'tips'),
    ('news', 'news'),
]

class Newsletter(models.Model):
    newsletter_text = models.TextField(max_length=10000, default='')
    newsletter_picture = models.ImageField(upload_to='newsletter_pictures', default='default.jpg')
    newsletter_category = models.CharField(max_length=100, default='')