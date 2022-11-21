from django.urls import path

from newsletter.views import add_newsletter, view_newsletter_list
urlpatterns = [
     path('add-newsletter/', add_newsletter),
     path('view-newsletter-list/', view_newsletter_list),
]