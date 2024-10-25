from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models.appointment_model import Appointment

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    time = request.form.get('time')

    if name and time:
        try:
            new_appointment = Appointment(name=name, time=time)
            db.session.add(new_appointment)
            db.session.commit()
            flash(f"Appointment booked successfully for {name} at {time}.")
        except Exception as e:
            db.session.rollback()  # Roll back in case of error
            flash("An error occurred while booking your appointment.", "error")
            logging.error(f"Failed to book appointment: {e}")
    else:
        flash("Name and time are required.", "error")
    return redirect(url_for('home'))