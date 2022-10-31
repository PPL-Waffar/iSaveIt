from django.urls import path
from user.views import *
urlpatterns = [
     path('flu-register-user/', flutter_register_user),
     path('flu-login/',flutter_user_login),
     path('user-info/',flutter_get_user_info)
]