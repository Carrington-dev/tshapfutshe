from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from security.forms import OrderForm
from security.models import Order
from security.pay_utils import get_data_validate

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
    context = dict()
    return render(request, 'donations/donations.html', context)

def donate(request):
    context = dict()
    # Handle the donation form submission here if needed
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print("Form data is valid:", form.is_valid())  # Debugging line to check form data
        if form.is_valid():
            order = form.save()
            # order.order_number = str(order.pk)[-12:-1]
            order.save()
            messages.success(request, f'Thank you {order.first_name} {order.last_name}, your order number is {order.order_number}. Please proceed to pay.')
            # url = f"{request.scheme}://{request.META['HTTP_HOST']}{str(reverse(order.payment_method.lower().strip(), args=[order.pk]))}"
            # order_started_html.delay(url, order.pk)
            # order_started.delay(url, order.pk)
            
            order.status = 'Pending'
            order.currency = 'USD'
            order.save()
            
            # return redirect(reverse('paypal', pk=order.pk))
            return redirect('paypal', pk=order.pk)
            # return redirect(reverse('paypal', args=[order.pk]))
            # return redirect('home')  # 'home' is the name of a URL pattern

        else:
            print("Form is not valid")
            messages.error(request, _('There was an error with your submission. Please try again.'))

    context['form'] = form
    return render(request, 'donations/donate.html', context)

def paypal(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = dict()
    context['htmlForm'] = get_data_validate(request, order.order_number, order.order_total, order.pk)
    context['order'] = order
    return render(request, 'donations/paypal.html', context)

def payment_done(request, pk):
    return render(request, 'donations/payment_done.html')

def payment_canceled(request, pk):
    return render(request, 'donations/payment_canceled.html')

def before(request, pk):
    return JsonResponse({'status': 'ok', 'message': 'Payment is being processed.'})
