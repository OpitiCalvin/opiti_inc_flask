from opiti_inc import db
from opiti_inc.views import site
from flask import (
    make_response, flash, current_app, redirect, render_template, request, session, url_for
)
from opiti_inc.models.contacts import ContactModel


@site.route('/contact', methods=['GET', 'POST'])
def contact():
	r"""
	"""

	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			# print(data)

			msg = ContactModel(
				name = data['fname'] +' ' + data['lname'],
				email = data['email'],
				# phone = data['phone'],
				# country = data['country'],
				message = data['message'],
				created_by = 'web link',
			)
			db.session.add(msg)
			db.session.commit()
			
			flash("Message successfully sent.")
			return redirect(url_for('site.contact'))

		except Exception as error:
			db.session.rollback()
			print(error)
			flash("An error occurred.")
			return redirect(url_for('site.contact'))

	return render_template('pages/contact.html')
