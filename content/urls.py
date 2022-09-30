from django.urls import path
from . import views


urlpatterns = [
    path("api/content/", views.ContentView.as_view())

]
