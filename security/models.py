import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


import uuid
from .utils import order_num_gen
from .vars import *
from .fields import OrderField
from tshaweb import settings

# Create your models here.



from security.managers import UserManager

class User(AbstractUser):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    email = models.EmailField( max_length=254, unique=True)
    first_name = models.CharField( max_length=254)
    last_name = models.CharField( max_length=254)
    username = models.CharField(max_length=254, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "username" ]

    def __str__(self):
        return f"{self.email} {self.username} @ {str(self.id)[:20]}"

    def __unicode__(self):
        return f"{self.email} {self.username} @ {str(self.id)[:20]}"
    
    class Meta:
        ordering = [ "email", "username" ]



class Payment(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD, default="CC" )
    card_number = models.CharField(max_length=200, null=True, blank=True)
    
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.payment_id

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'


class Order(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 

    payment                 = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    email                   = models.EmailField(max_length=200, blank=False)
    first_name              = models.CharField(max_length=200, blank=False)
    last_name               = models.CharField(max_length=200, blank=False)
    country                 = models.CharField(max_length=600,  default='South Africa')
    state                   = models.CharField(max_length=600,  default='Gauteng')
    short_description       = models.TextField(default='Gauteng')
    # country                 = models.CharField(max_length=400, choices=countries, default='ZA')
    type_of_class           = models.CharField(max_length=300, blank=True, null=True)
    phone                   = models.CharField(max_length=50, default="")
    order_total             = models.DecimalField(max_digits=10, decimal_places=2, default=3)
    device_name             = models.CharField(max_length=700, null=True, blank=True)
    currency                = models.CharField(max_length=40, default="USD")
    ip_adress               = models.CharField(max_length=40, default="0.0.0.1")
    order_type              = models.CharField(max_length=300, choices=ORDER_TYPE, default="Reciept")
    payment_method          = models.CharField(max_length=300, choices=payment_method, default="PayPal")
    city                    = models.CharField(max_length=200, blank=True, null=True)
    street_name             = models.CharField(max_length=400, blank=True, null=True)
    zip_code                = models.CharField(max_length=200, blank=True, null=True)
    status                  = models.CharField(max_length=100, choices=STATUS, default="Started")
    delivery_status         = models.CharField(max_length=100, choices=D_STATUS, default="Scheduled")
    order_number            = models.CharField(max_length=300, default=order_num_gen(), blank=True, null=True)
    date_ordered			= models.DateTimeField(verbose_name='date orderd', auto_now_add=True)
    last_viewed	            = models.DateTimeField(verbose_name='last viewed', auto_now=True)
    is_ordered              = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def save(self, *args, **kwargs):
        order = super(Order, self).save(*args, **kwargs)
        
        
    