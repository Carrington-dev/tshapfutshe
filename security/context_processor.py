from datetime import datetime
from decouple import config


def show_data(request):
    """
    Context processor to add user data to the context.
    """
    company = "Tshapfutshe SDA Church"
    return {
        "company": company,
        "company_title": company,
        "year": 2025,
        "phone": '+27 (0) 67 735 2242',
        "title": 'Home of Faith',
        "slogan": 'Muṱa wa Lutendo wa Tshafutshe',
        "PAYPAL_CLIENT_ID": config("PAYPAL_CLIENT_ID"),
        "description": 'Muṱa wa Lutendo wa Tshafutshe',
        "keywords": 'Muṱa wa Lutendo wa Tshafutshe',
        "email": 'hello@tshapfutshesda.co.zw',
        "shop_email": 'uniforms@tshapfutshesda.co.zw',
        "address": "Tshapfutshe SDA Church</p><p>Beitbridge MS, ZW160101</p><p>Zimbabwe",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }