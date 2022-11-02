from django.urls import path
from .views import add_feedback_report, delete_feedback_report

urlpatterns = [
    path('add-feedback-report/', add_feedback_report),
    path('delete-feedback-report/', delete_feedback_report)
]