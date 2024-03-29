from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name='index'),
    path("authenticate/", include("authenticate.urls")),
    path("contact/", include("contact.urls")),
    path("account/", include("account.urls")),
]
