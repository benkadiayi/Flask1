from flask import Blueprint, render_template


site = Blueprint('site', __name__, template_folder='sites_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/prices')
def prices():
    return render_template('prices.html')

@site.route('/about')
def about():
    return render_template('about.html')