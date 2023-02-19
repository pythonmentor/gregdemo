"""
Greg Exemple URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("gregdemo.pages.urls")),
    path("users/", include("gregdemo.users.urls")),
    path("followers/", include("gregdemo.followers.urls")),
]
