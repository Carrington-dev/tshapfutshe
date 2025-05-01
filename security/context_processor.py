from datetime import datetime


def show_data(request):
    """
    Context processor to add user data to the context.
    """
    company = "Tshafutshe SDA Church"
    return {
        "company": company,
        "company_title": company,
        "year": 2025,
        "phone": '+27 (0) 67 735 2242',
        "title": 'Home of Faith',
        "slogan": 'Muṱa wa Lutendo wa Tshafutshe',
        "description": 'Muṱa wa Lutendo wa Tshafutshe',
        "keywords": 'Muṱa wa Lutendo wa Tshafutshe',
        "email": 'hello@tshapfutshesda.co.zw',
        "shop_email": 'uniforms@tshapfutshesda.co.zw',
        "address": "410 Francis Baard Street</p><p>Pretoria Central, 0001</p><p>South Africa",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }