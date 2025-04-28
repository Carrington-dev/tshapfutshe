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
        "title": 'Muṱa wa Lutendo wa Tshafutshe',
        "slogan": 'Muṱa wa Lutendo wa Tshafutshe',
        "description": 'Top Tutors is a leading tutoring company in South Africa, providing personalized tutoring services to students of all ages. Our experienced tutors are dedicated to helping students achieve their academic goals and reach their full potential.',
        "email": 'hello@toptutors.co.za',
        "shop_email": 'uniforms@toptutors.co.za',
        "address": "410 Francis Baard Street</p><p>Pretoria Central, 0001</p><p>South Africa",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }