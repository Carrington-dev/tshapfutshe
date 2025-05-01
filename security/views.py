from django.http import HttpResponse
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext_lazy as _

def my_view(request):
    output = _("Welcome to ") + "Tshapfutshe SDA Church!"
    return HttpResponse(output)

def index(request):
    return render(request, 'security/index.html')

def about(request):
    return render(request, 'security/about.html')

def contact(request):
    return render(request, 'security/contact.html')

def services(request):
    return render(request, 'security/services.html')

def testimonials(request):
    return render(request, 'security/testimonials.html')

def policy(request):
    return render(request, 'security/policy.html')

def terms(request):
    return render(request, 'security/terms.html')

def faqs(request):
    return render(request, 'security/faqs.html')

def portfolio(request):
    return render(request, 'security//portfolio.html')
