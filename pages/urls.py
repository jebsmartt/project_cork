# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('classes/', views.class_options_view, name='class_options'), # <-- New path
]