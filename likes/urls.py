from django.urls import path
from .views import LikeBandView, LikeBandDetailView

urlpatterns = [
    path("", LikeBandView.as_view()),
    path("<int:band_id>/", LikeBandDetailView.as_view()),
]
