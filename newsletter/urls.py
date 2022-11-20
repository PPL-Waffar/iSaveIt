from django.urls import path

from newsletter.views import add_newsletter
urlpatterns = [
     path('add-newsletter/', add_newsletter,
     )
]