from django.urls import path
from . import views

# URLs
urlpatterns = [
    path("schools/", views.list)
]
