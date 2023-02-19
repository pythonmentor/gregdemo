from django.urls import path
from .views import followers_index

app_name = "followers"

urlpatterns = [
    path("", followers_index, name="index"),
]
