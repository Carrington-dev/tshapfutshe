from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    # Example: path('admin/', admin.site.urls),
    # path('api/', include('your_app.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('policy/', views.policy, name='policy'),
    path('terms/', views.terms, name='terms'),
    path('faqs/', views.faqs, name='faqs'),
    path('my_view/', views.my_view, name='my_view'),
    path('', views.index, name='home'),  # Default route to index page

    path('department/pathfinders/', views.pathfinder, name='pathfinder'),
    path('department/adventurers/', views.adventurer, name='adventurer'),
    path('department/youth/', views.youth, name='youth'),
    path('department/sabbath_school/', views.sabbath_school, name='sabbath_school'),
    path('department/personal_ministries/', views.personal_ministries, name='personal_ministries'),
    path('department/education/', views.education, name='education'),
    path('department/family/', views.family, name='family'),
    path('department/welfare/', views.welfare, name='welfare'),
    path('department/health/', views.health, name='health'),
    path('department/prayer/', views.prayer, name='prayer'),
    path('department/music/', views.music, name='music'),

    path('donate/', views.donate, name='donate'),
    path('donations/', views.donations, name='donations'),
    path('paypal/<str:pk>', views.paypal, name='paypal'),
    path('payfast/<str:pk>', views.payfast, name='payfast'),
    path('before/<str:pk>', views.before, name='before'),
    path('canceled/<str:pk>', views.payment_canceled, name='canceled'),
    path('payment_done/<str:pk>', views.payment_done, name='payment_done'),
    path('pay_clear/<str:pk>', views.pay_clear, name='pay_clear'),

]
