from django.http import HttpResponseRedirect
from django.utils.translation import get_language
from django.urls import reverse

class ForceDefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_code = request.LANGUAGE_CODE

        # If no language code in URL, force redirect to default language (Tshivenda)
        if not language_code or language_code == 'en':  # Adjust if needed
            return HttpResponseRedirect(f"/ve{request.path}")

        response = self.get_response(request)
        return response
