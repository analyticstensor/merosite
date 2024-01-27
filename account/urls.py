from django.contrib import admin
from django.urls import path, include

from .views import UserAccountView, UserListView, UserUpdateView

urlpatterns = [
    path("", UserAccountView.as_view(), name="account"),
    path("profile/", UserListView.as_view(), name="profile"),
    path("profile/update/<int:pk>/", UserUpdateView.as_view(), name="update"),
]