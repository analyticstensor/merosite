from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm, CustomPasswordChangeForm, CustomSetPasswordForm

decorators = [login_required(login_url='login'),]

class AuthLoginView(LoginView):
    template_name = "authenticate/login.html"
    authentication_form = CustomAuthenticationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "authenticate/signup.html"

class AuthPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "authenticate/password_change.html"

class AuthPasswordChangeDoneView(TemplateView):
    template_name = "authenticate/password_change_done.html"

class AuthPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = "authenticate/password_reset_form.html"
    email_template_name = "authenticate/password_reset_email.html"
    subject_template_name = "authenticate/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")    

class AuthPasswordResetDoneView(TemplateView):
    template_name = "authenticate/password_reset_done.html"

class AuthPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = "authenticate/password_reset_confirm.html"

class AuthPasswordResetComplete(TemplateView):
    template_name = "authenticate/password_reset_complete.html"