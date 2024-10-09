from django.urls import path
from dashboard.views import IndexView


urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
]
