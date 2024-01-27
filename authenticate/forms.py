from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from crispy_forms.helper import FormHelper
from django.urls import reverse

from .models import CustomUser

from crispy_forms.layout import Submit, Layout, Field, Hidden

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {
            'username': None
        }
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-passowrd', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-passowrd', 'placeholder': 'Password'})
        self.helper = FormHelper(self)
        self.helper.form_show_errors = False
        self.helper.form_id = 'signup-form'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

class CustomUserChangeForm(UserChangeForm):
    #password = None        

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email' )
        help_texts = {
            'username': None
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user-update-form'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(Field('password', type='hidden'), Field('username', readonly=True), Field('email', readonly=True), 'first_name', 'last_name')
        self.helper.add_input(Submit('save', 'Save', css_class='btn-success'))

class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'autocomplete': 'current-passowrd', 'placeholder': 'Password'})
        self.error_messages = {
            "invalid_login": (""),
            "inactive": ("This account is inactive."),
        }
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.form_id = 'login-form'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary')),
        self.helper.add_input(Submit('submit', 'Forgot Password', css_class='btn-primary', onclick="window.location.href = '{}';".format(reverse('password_reset'))))

class CustomPasswordResetForm(PasswordResetForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'autofocus': True, 'placeholder': 'Email'})    
        self.helper = FormHelper()
        self.helper.form_id = 'password-reset-form'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

class CustomPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'New Password'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'New Password'})  
        self.helper = FormHelper()
        self.helper.form_id = 'password-change-form'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

class CustomSetPasswordForm(SetPasswordForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'New Password'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'New Password'})  
        self.helper = FormHelper()
        self.helper.form_id = 'set-password-form'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))             