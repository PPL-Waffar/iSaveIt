from django.urls import path
from .views import add_feedback_report

urlpatterns = [
    path('add-feedback-report/', add_feedback_report),
]