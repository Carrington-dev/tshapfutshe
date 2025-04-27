from datetime import datetime
from src import app
from flask import render_template

@app.context_processor
def inject_globals():
    company = "Top Tutors"
    return {
        "company": company,
        "company_title": company,
        "year": 2025,
        "phone": '+27 (0) 67 735 2242',
        "title": 'South Africa’s Leading Tutoring Company',
        "description": 'Top Tutors is a leading tutoring company in South Africa, providing personalized tutoring services to students of all ages. Our experienced tutors are dedicated to helping students achieve their academic goals and reach their full potential.',
        "email": 'hello@toptutors.co.za',
        "shop_email": 'uniforms@toptutors.co.za',
        "address": "410 Francis Baard Street</p><p>Pretoria Central, 0001</p><p>South Africa",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html", title="Services")

@app.route("/schools")
def schools():
    return render_template("schools.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

# Add More About Us Pages

@app.route("/academic-excellence")
def academic_excellence():
    return render_template("about/academic_excellence.html")

@app.route("/our-offering")
def our_offering():
    return render_template("about/our_offering.html")

@app.route("/our-principles")
def our_principles():
    return render_template("about/our_principles.html")

@app.route("/leadership")
def leadership():
    return render_template("about/leadership.html")

@app.route("/our-values")
def our_values():
    return render_template("about/our_values.html")

@app.route("/uniforms")
def uniform():
    return render_template("about/uniform.html")

@app.route("/boarding")
def boarding():
    return render_template("about/boarding.html")

# Default route for 404 errors
@app.route("/<path:path>")
def catch_all(path):
    return render_template("404.html"), 404

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"), 404