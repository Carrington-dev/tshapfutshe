from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    # Example: path('admin/', admin.site.urls),
    # path('api/', include('your_app.urls')),
    path('/about/', views.about, name='about'),
    path('/contact/', views.contact, name='contact'),
    path('/services/', views.services, name='services'),
    path('/portfolio/', views.portfolio, name='portfolio'),
    path('/testimonials/', views.testimonials, name='testimonials'),
    path('/policy/', views.policy, name='policy'),
    path('/terms/', views.terms, name='terms'),
    path('/faqs/', views.faqs, name='faqs'),
    path('', views.index, name='home'),  # Default route to index page

]
