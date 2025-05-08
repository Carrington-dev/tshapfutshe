from datetime import datetime
from decouple import config
from django.utils.translation import gettext_lazy as _


def show_data(request):
    """
    Context processor to add user data to the context.
    """
    company = _("Tshapfutshe SDA Church")
    
    
    return {
        "company": company,
        "company_title": company,
        "year": 2025,
        "phone": '+27 (0) 67 735 2242',
        "title": _('Home of Faith'),
        "PAYPAL_CLIENT_ID": config("PAYPAL_CLIENT_ID"),
        "keywords": 'Muṱa wa Lutendo wa Tshafutshe',
        "email": 'hello@tshapfutshesda.co.zw',
        "shop_email": 'uniforms@tshapfutshesda.co.zw',
        "address": f"{company}</p><p>Beitbridge MS, ZW160101</p><p>Zimbabwe",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }