from decimal import Decimal
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from security.forms import OrderForm
from security.models import Order, Payment
from security.pay_utils import get_data_validate
from tshaweb import settings


def index(request):
    context = dict()
    context['title'] = _('Home of Faith')
    return render(request, 'security/index.html', context)

def about(request):
    context = dict()
    context['title'] = _("About Us")
    return render(request, 'security/about.html', context)

def contact(request):
    context = dict()
    context['title'] = _('Contact Us')
    if request.method == 'POST':
        # Handle the contact form submission here
        # You can use Django's forms or just process the data directly
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you can send an email or save the message to the database
        
        messages.success(request, _('Thank you for contacting us! We will get back to you soon.'))
        return redirect('contact')  # Redirect to the same page or another page after submission
    return render(request, 'security/contact.html', context)

def services(request):
    context = dict()
    context['title'] = _('Services')
    return render(request, 'security/services.html', context)

def testimonials(request):
    context = dict()
    context['title'] = _('Testimonials')
    return render(request, 'security/testimonials.html', context)

def policy(request):
    context = dict()
    context['title'] = _('Privacy Policy')
    return render(request, 'security/policy.html', context)

def terms(request):
    context = dict()
    context['title'] = _('Terms and Conditions')
    return render(request, 'security/terms.html', context)

def faqs(request):
    context = dict()
    context['title'] = _('FAQs')
    return render(request, 'security/faqs.html', context)

def portfolio(request):
    context = dict()
    context['title'] = _('Portfolio')
    return render(request, 'security/portfolio.html', context)

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
    context['title'] = _('Donations')
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
            order.order_number = order.order_number
            order.save()
            messages.success(request, f'Thank you {order.first_name} {order.last_name}, your order number is {order.order_number}. Please proceed to pay.')
            # url = f"{request.scheme}://{request.META['HTTP_HOST']}{str(reverse(order.payment_method.lower().strip(), args=[order.pk]))}"
            # order_started_html.delay(url, order.pk)
            # order_started.delay(url, order.pk)
            
            order.status = 'Pending'
            order.currency = 'USD'
            order.save()
            
            # return redirect(reverse('paypal', pk=order.pk))
            # return redirect('paypal', pk=order.pk)
            return redirect(reverse(order.payment_method.lower(), args=[order.pk]))
        else:
            print("Form is not valid")
            messages.error(request, _('There was an error with your submission. Please try again.'))

    context['form'] = form
    context['order'] = order if 'order' in locals() else None
    return render(request, 'donations/donate.html', context)

def payfast(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = dict()
    
    context['htmlForm'] = get_data_validate(request, order.order_number, (round( Decimal(order.order_total) * Decimal(18.5))), order.pk)
    context['order'] = order
    context['title'] = _('PayFast Payment')
    context['PAYFAST_MERCHANT_ID'] = settings.PAYFAST_MERCHANT_ID
    return render(request, 'donations/payfast.html', context)

def paypal(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = dict()
    context['htmlForm'] = get_data_validate(request, order.order_number, order.order_total, order.pk)
    context['order'] = order
    context['title'] = _('PayPal Payment')
    context['PAYPAL_CLIENT_ID'] = settings.PAYPAL_CLIENT_ID
    return render(request, 'donations/paypal.html', context)

def payment_done(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = dict()
    context['order'] = order
    context['title'] = _('Payment Done')
    context['message'] = _('Thank you for your donation! Your payment has been successfully processed.')
    return render(request, 'donations/payment_done.html', context)

def payment_canceled(request, pk):
    context = dict()
    context['title'] = _('Payment Canceled')
    context['message'] = _('Your payment has been canceled. If you have any questions, please contact us.')
    return render(request, 'donations/payment_canceled.html', context)

def before(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.is_ordered = True
    order.save()
    return JsonResponse({'status': 'ok', 'message': 'Payment is being processed.'})

def pay_clear(request, pk):
    order = get_object_or_404(Order, pk=pk)
    data_body = json.loads(request.body)

    payment = Payment(
        # user = request.user if request.user.is_authenticated()  else None,
        payment_id = data_body['transactionID'],
        payment_method = data_body['payment_method'],
        amount_paid = data_body['total'],
        status = data_body['status'],
    )
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.status = "Completed"
    order.device_name = request.headers['User-Agent']
    order.save()
    messages.success(request, f'You have successfully paid for your order with order number {order.order_number}')
    
    data = {
        "message": f"You have successfully paid for your order with order number {order.order_number}",
        "order_number": order.order_number,
        "transID": payment.payment_id,
    }
    # return Response(data, )
    return JsonResponse(data=data, safe=False)

def change_language(request, lang_code):
    translation.activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))