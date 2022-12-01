from django.urls import path

from newsletter.views import add_newsletter, view_detail_newsletter, view_newsletter_list,delete_newsletter,newsletterhtmk
urlpatterns = [
     path('add-newsletter/', add_newsletter),
     path('view-detail-newsletter/id=<int:id>/', view_detail_newsletter),
     path('view-newsletter-list/', view_newsletter_list),
     path('<int:id>', delete_newsletter, name = 'delete_newsletter'),
     path('list/', newsletterhtmk),
]
