from opiti_inc.views import site
from flask import (
    make_response, flash, current_app, redirect, render_template, request, session, url_for
)

# a simple page that says hello
@site.route('/')
def index():
	return render_template('index.html')

# @site.route('/contact', methods=['GET', 'POST'])
# def contact():
# 	return render_template('pages/contact.html')

@site.route('/solution')
def solution():
	return render_template('pages/products.html')

@site.route('/skills')
def expertise():
	return render_template('pages/expertise.html')