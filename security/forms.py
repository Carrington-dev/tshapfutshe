from django.forms import ModelForm
from security.models import Order
from django.utils.translation import gettext_lazy as _

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = [ "payment_method"]
        fields = [
            'email',
            'first_name',
            'last_name',
            'country',
            'phone',
            'order_total',
            'payment_method',
            'state',
            'city',
            'street_name',
            'zip_code',
            # 'status',
            'short_description',
        ]
        labels = {
            'first_name': _("First Name"),
            'last_name': _("Last Name"),
            'email': _("Email Address"),
            'country': _("Country"),
            'phone': _("Phone Number"),
            'order_total': _("Order Total"),
            'payment_method': _("Payment Method"),
            'state': _("State"),
            'city': _("City"),
            'street_name': _("Street Name"),
            'zip_code': _("Zip Code"),
            'short_description': _("Short Description"),
            # 'status': _("Status"),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': f"Enter your {' '.join(field.split('_'))}"})