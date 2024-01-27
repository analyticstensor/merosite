from django.urls import path, include
from django.contrib import admin

from .views import (AuthLoginView, SignUpView, AuthPasswordChangeView, AuthPasswordChangeDoneView, AuthPasswordResetView, 
        AuthPasswordResetDoneView, AuthPasswordResetConfirmView, AuthPasswordResetComplete)

from django.contrib.auth.views import LogoutView

#app_name = 'authenticate'
urlpatterns = [
    path("login/",  AuthLoginView.as_view(), name="login"),
    path("logout/",  LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("password_change/", AuthPasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", AuthPasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", AuthPasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", AuthPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", AuthPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", AuthPasswordResetComplete.as_view(), name="password_reset_complete"),
    # path("", include("django.contrib.auth.urls")), # must be always at end to support AuthenticateLoginView
]

# Update admin page
admin.site.site_title = 'Administration'
admin.site.site_header = 'Administration Login'
admin.site.index_title = 'Administration Page'