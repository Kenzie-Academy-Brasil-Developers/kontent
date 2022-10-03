from django.urls import path
from . import views


urlpatterns = [
    path("contents/", views.ContentView.as_view()),
    path("contents/<int:content_id>/", views.ContentDetails.as_view()),
    path("contents/filter/", views.ContentFilter.as_view())
]
