# Return site_information setting into request context in all views.

from django.conf import settings

def site_information(request):
    return {'site_info': settings.SITE_INFORMATION}
