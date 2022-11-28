from django.urls import path

from newsletter.views import add_newsletter, view_detail_newsletter
urlpatterns = [
     path('add-newsletter/', add_newsletter),
     path('view-detail-newsletter/id=<int:id>/', view_detail_newsletter),
]
