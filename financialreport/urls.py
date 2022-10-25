from django.urls import path

from financialreport.views import view_financial_report, download_financial_report


urlpatterns = [
     path('view-financial-report/', view_financial_report),
     path('download-financial-report/', download_financial_report)
]