payment_method = [
    # ("PayPal","PayPal"),
    ("PayFast","PayFast"),
    # ("PayPal","PayPal"),
    # ("Ozow","Ozow"),
    # ("Yoco","Yoco"),
    ("EFT","EFT"),
]

LABELS = (

        ('New','New'),
        ('Featured','Featured'),
        ('Ultimate','Ultimate'),
        ('Business','Business'),
        ('Free','Free'),
        # ('Returned','Returned'),


    )

STATUS = (

        ('New','New'),
        ('Started','Started'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
        ('Returned','Returned'),


    )

PAYMENT_METHOD = (
        ('Ozow','Ozow'),
        ('PayPal','PayPal'),
        ('Braintree','Braintree'),
        ('CC','Credit Card'),
        ('DC','Debit Card'),
        ('eBucks','eBucks'),
        ('Mobicred','Mobicred'),
        ('Stripe','Stripe'),
    )


D_STATUS = (

        
        ('Delivered','Delivered'),
        ('Scheduled','Scheduled'),
        ('Cancelled','Cancelled'),
        ('Rescheduled','Rescheduled'),


    )
PREFFERED_METHOD = (
        ('Code 8','Code 8'),
        ('Code 10','Code 10'),
        ('Code 11','Code 11'),
        ('Code 14','Code 14'),
        
    )

p_cs = [
    ("Code 10 Lessons","Code 10 Lessons"),
    ("Code 14 Lessons","Code 14"),
    ("Code 8 Lessons","Code 8 Lessons"),
    ("Learners","Learners"),
    ("Bike Lessons","Bike Lessons"),
]

STATUS_CHOICES = (
 ('draft', 'Draft'),
 ('published', 'Published'),
 )


ORDER_TYPE = (
 ('Reciept', 'Reciept'),
 ('Invoice', 'Invoice'),
 ('Quote', 'Quote'),
 )