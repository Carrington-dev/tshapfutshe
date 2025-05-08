
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# from tshaweb import settings

# urlpatterns = [
#     # path('i18n/', include('django.conf.urls.i18n')),  # URL for language switching
#     path('admin/', admin.site.urls),
#     path('', include('security.urls')),  # Include the security app URLs
# ]

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # to support language switching forms
]

urlpatterns += i18n_patterns(
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('security.urls')),  # Include the security app URLs
    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)