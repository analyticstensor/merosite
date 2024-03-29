from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from django.http import HttpResponse
from django.conf import settings

from django import forms
from django.forms import ModelForm
from .models import Contact

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ['message_received_datetime']
        widgets = {
            'name': forms.TextInput(attrs = {'autofocus': True, 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs = {'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs = {'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs = {'placeholder': 'Message'}),
            'user_id': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contact-form'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))        
        
    def send_email(self, subject, message, email, name):
        html_message = render_to_string('contact/contact_email_format.html', {'name': name, 'email': email, 'message': message, 'subject': subject, 'sent_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        message = strip_tags(html_message)
        try:
            send_mail(subject=subject, message=message, from_email=None, recipient_list=[settings.EMAIL_HOST_USER])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        else:
            send_mail(subject='We have received your message.', message=f'Hi {name},\n\n We have received your message. We will contact you soon.\n\nThanks,\nSupport.\n\nThis is an autogenerated email.', from_email=None, recipient_list=[email])