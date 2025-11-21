# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path(URL_route, view_function_name, name_for_referencing)
    path("", views.home_page_view, name="home"),
]