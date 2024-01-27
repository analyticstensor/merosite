from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from authenticate.models import CustomUser
from authenticate.forms import CustomUserChangeForm

decorators = [login_required(login_url='login'),]

@method_decorator(decorators, name="dispatch")
class UserAccountView(TemplateView):
    template_name = "account/index.html"

@method_decorator(decorators, name="dispatch")
class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    #template_name_suffix = "_update_profile"
    template_name = "account/update.html"
    success_url = reverse_lazy("account")

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.user)

@method_decorator(decorators, name="dispatch")
class UserListView(ListView):
    model = CustomUser
    context_object_name = 'user_profile'
    template_name = "account/profile.html"

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.user)
        
