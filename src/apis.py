from threading import Thread
import uuid
from flask import request, jsonify
from src import app
from sparkpost import SparkPost
from flask import render_template, jsonify, request, redirect, url_for, flash
from decouple import config
from string import Template

SPARKPOST_API_KEY = config("MAIL_PASSWORD")  # Consider using environment variables
ADMIN_EMAIL = config('ADMIN_EMAIL')
sp = SparkPost(SPARKPOST_API_KEY)


def load_html_template(context, template="send.html") -> str:
    return render_template(template, **context)
    # with open(("send.html"), "r", encoding="utf-8") as file:
    #     template = Template(file.read())
    #     return template.safe_substitute({"substitution_data": { 
    #             "name": "john",
    #             "otp": "123456"
    #         }})

def send_email_async(app, to, subject, message, email, full_name, template):
    with app.app_context():
      try:
          context = {
              "name": full_name,
              "subject": subject,
              "email": email,
              "subject": subject,
              "message": message,
          }
          html_content = load_html_template(template=template, context=context)
          sp.transmissions.send(
              # recipients=[to],
              recipients=[
                  {
                      'address': to,
                      # 'substitution_data': {
                      #     'username': 'Carrington06',
                      #     'name': 'Carrington',
                      #     'otp': '876098'
                      # }
                  },
              ],
              html=html_content,
              from_email='CR Driving <noreply@ruma.stemgon.co.za>',
              subject=subject
          )
      except Exception as e:
          return (f"Email sending failed: {e}")


@app.route("/api")
def api_home():
    """
    Welcome API
    ---
    tags:
      - Basic Views
    responses:
      200:
        description: Returns a feedback message
        schema:
          type: object
          properties:
            message:
              type: string
              example: "You are now subscribed to our newsletter!."
    """
    return jsonify({
        "message": "You are now subscribed to our newsletter!."
    })


@app.route("/api/subscribe", methods=['POST'])
def subscribe():
    """
    Simple Subscribe API
    ---
    tags:
      - Basic Views
    responses:
      200:
        description: Returns a feedback message
        schema:
          type: object
          properties:
            message:
              type: string
              example: "You are now subscribed to our newsletter!."
    """
    return jsonify({
        "message": "You are now subscribed to our newsletter!."
    })


@app.route('/send-email', methods=['POST'])
def send_email():
    """
    Send email after user contact us
    ---
    tags:
      - Mailing
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - subject
            - message
            - email
          properties:
            name:
              type: string
              example: Maanda
            subject:
              type: string
              example: FAQs Not Updated
            message:
              type: string
              example: Good day I hope you are well. You FAQ is not updated,
            email:
              type: string
              example: johndoe@example.com
            
    responses:
      201:
        description: Your information was sent!.
      400:
        description: Your information was not sent!.
    """
    data = request.form
    print(data)
    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400
    
    to = ADMIN_EMAIL
    subject = data.get('subject', "Contact Us")
    message = data.get('message', "Contact Us Form")
    email = data.get('email', ADMIN_EMAIL)
    full_name = data.get('name', "Harry Porter")
    template = "message.html"

    # Send email in a background thread
    Thread(target=send_email_async, args=(app, to, subject, message, email, full_name, template)).start()
    flash('Form submitted successfully!', 'success')  
    return jsonify({'status': 'Your information was sent!.'}), 200
    # return redirect(url_for('contact'))


@app.route('/confirm-registration', methods=['POST'])
def send_registration_email():
    """
    Send email after user creation
    ---
    tags:
      - Mailing
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - subject
            - message
            - email
          properties:
            name:
              type: string
              example: Maanda
            subject:
              type: string
              example: FAQs Not Updated
            message:
              type: string
              example: Good day I hope you are well. You FAQ is not updated,
            email:
              type: string
              example: johndoe@example.com
            
    responses:
      201:
        description: Your information was sent!.
      400:
        description: Your information was not sent!.
    """
    
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400
    
    # to = data.get('to', ADMIN_EMAIL)
    # subject = data.get('subject', "Testing App")
    # message = data.get('message', "Testing App")
    
    # Send email in a background thread
    to = data.get('email', ADMIN_EMAIL)
    subject = data.get('subject', "Testing App")
    message = data.get('message', "Testing App")
    email = data.get('email', ADMIN_EMAIL)
    full_name = data.get('name', "Harry Porter")
    template = "send.html"

    # Send email in a background thread

    try:
        # Send email in a background thread
        Thread(target=send_email_async, args=(app, to, subject, message, email, full_name, template)).start()
        
        # Thread(target=send_email_async, args=(app, to, subject, message)).start()
        return jsonify({'status': 'We are pleased to inform you that your registration has been successfully completed!'}), 200
    except Exception as e:
        return jsonify({"status": f"Registration failed: {e}"}), 400