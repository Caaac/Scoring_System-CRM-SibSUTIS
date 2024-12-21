from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^update_scoring_rate/(?P<pk>[0-9]+)$', views.update_scoring_rate),
]