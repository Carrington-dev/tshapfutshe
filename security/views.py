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
    return render(request, 'security/portfolio.html')

# Add more views as needed for departments

def pathfinder(request):
    return render(request, 'department/pathfinders.html')

def adventurer(request):
    return render(request, 'department/adventurers.html')

def youth(request):
    return render(request, 'department/youth.html')

def sabbath_school(request):
    return render(request, 'department/sabbath_school.html')

def personal_ministries(request):
    return render(request, 'department/personal_ministries.html')

def education(request):
    return render(request, 'department/education.html')

def family(request):
    return render(request, 'department/family.html')

def welfare(request):
    return render(request, 'department/welfare.html')

def health(request):
    return render(request, 'department/health.html')

def prayer(request):
    return render(request, 'department/prayer.html')

def music(request):
    return render(request, 'department/music.html')

# Add more views as needed for other donations or departments
def donations(request):
    return render(request, 'donations/donations.html')

def donate(request):
    return render(request, 'donations/donate.html')

def paypal(request):
    return render(request, 'donations/paypal.html')

def payment_done(request):
    return render(request, 'donations/payment_done.html')

def payment_canceled(request):
    return render(request, 'donations/payment_canceled.html')
