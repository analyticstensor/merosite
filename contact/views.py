import logging
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.shortcuts import render

from .forms import ContactForm

logger = logging.getLogger('application')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "contact/contact.html"
    success_url = "email/success/"
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logger.info(f"User name {request.user.username} is filling the contact information.")
            form = ContactForm(initial={'name': request.user.get_full_name, 'email': request.user.email, 'user_id': request.user.id})
            context = {'form': form}   
            return render(request, self.template_name, context)
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = 'Webapplication contact form:' + form.cleaned_data["subject"]    
        message = form.cleaned_data["message"]
        try:
            logger.info("Sending and saving contact message.")      
            form.send_email(subject, message, email, name)
            form.save()
        except Exception as exc:
            logger.exception(exc)
            raise
        return super().form_valid(form)    

class ContactEmailSuccessView(TemplateView):
    template_name = "contact/contact_email_success.html"
