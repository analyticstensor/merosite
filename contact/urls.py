from django.contrib import admin
from django.urls import path, include

from .views import ContactFormView, ContactEmailSuccessView

urlpatterns = [
    path("", ContactFormView.as_view(), name="contact"),
    path("email/success/", ContactEmailSuccessView.as_view(), name="contact_email_success"),
]