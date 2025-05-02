from django.forms import ModelForm
from security.models import Order

class OrderForm3(ModelForm):
    class Meta:
        model = Order
        # fields = [ "payment_method"]
        fields = [
            'email',
            'first_name',
            'last_name',
            'country',
            # 'type_of_class',
            'phone',
            'payment_method',
            'state',
            'city',
            'street_name',
            'zip_code',
            # 'status',
            'short_description',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': f"Enter your {' '.join(field.split('_'))}"})