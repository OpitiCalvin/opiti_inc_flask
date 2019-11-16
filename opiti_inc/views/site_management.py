from opiti_inc.views import site
from flask import (
    make_response, flash, current_app, redirect, render_template, request, session, url_for
)

# a simple page that says hello
@site.route('/')
def index():
	return render_template('index.html')

@site.route('/about-me')
def about():
	return render_template('pages/about.html')

@site.route('/sample-apps')
def solution():
	return render_template('pages/sample_apps.html')

@site.route('/skills')
def expertise():
	return render_template('pages/expertise.html')