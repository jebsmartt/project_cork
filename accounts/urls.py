# accounts/urls.py

from django.urls import path
from .views import SignUpView

urlpatterns = [
    # Maps /accounts/signup/ to your new SignUpView
    path('signup/', SignUpView.as_view(), name='signup'), 
]