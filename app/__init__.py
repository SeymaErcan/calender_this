# IMPORTS
from flask import Flask, render_template
import os
from app import routes

# SETUP
app = Flask(__name__)
app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(routes.bp)
