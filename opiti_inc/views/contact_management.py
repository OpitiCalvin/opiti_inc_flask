from opiti_inc import db
from opiti_inc.views import site
from flask import (
    make_response, flash, current_app, redirect, render_template, request, session, url_for
)
from opiti_inc.models.contacts import ContactModel
import requests


@site.route('/contact', methods=['GET', 'POST'])
def contact():
	r"""
	"""

	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			# print(data)

			msg = {
				"name": data['fname'] +' ' + data['lname'],
				"email": data['email'],
				"phone": data['phone'],
				"country": data['country'],
				"subject": data['subject'],
				"message": data['message']
			}
			print(f"msg: {msg}")

			try:
				url = "https://blog.opiticonsulting.com/api/contacts/"
				response = requests.post(url, json = msg)
				if response.status_code == 200:
					flash("Message successfully sent.")
					return redirect(url_for('site.contact'))					
				else:
					response.raise_for_status()
			except requests.exceptions.HTTPError as errh:
			    return "An Http Error occurred:" + repr(errh)
			except requests.exceptions.ConnectionError as errc:
			    return "An Error Connecting to the API occurred:" + repr(errc)
			except requests.exceptions.Timeout as errt:
			    return "A Timeout Error occurred:" + repr(errt)
			except requests.exceptions.RequestException as err:
			    return "An Unknown Error occurred" + repr(err)


			# db.session.add(msg)
			# db.session.commit()
			
			# flash("Message successfully sent.")
			# return redirect(url_for('site.contact'))

		except Exception as error:
			# db.session.rollback()
			print(error)
			flash("An error occurred.")
			return redirect(url_for('site.contact'))

	return render_template('pages/contact.html')
