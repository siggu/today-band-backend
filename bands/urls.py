from django.urls import path
from . import views
from .models import Band


urlpatterns = [
    path("", views.Bands.as_view()),
]
