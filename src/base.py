from decouple import config
from flask import Flask

app = Flask(__name__, 
            static_url_path="/static", 
            static_folder="static", 
            template_folder='templates')

app.config['SECRET_KEY'] = config('SECRET_KEY', default='oxpybBPmAWfvx4HlZ8TVxwR0UHfYJ6kO')
