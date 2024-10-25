import os
import logging
from flask import Flask, request, render_template, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tony:whpu4CqOykeHuw2sdeQUrETBkHfCp24u@dpg-csdhupd6l47c73dbe57g-a/schedule_db_zdhr'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

load_dotenv()
# Create the database tables
with app.app_context():
    db.create_all()  # Creates tables if they don't exist

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"An error occurred: {e}")
    return "An internal error occurred.", 500

# Home route to display appointments
@app.route('/')
def home():
    appointments = Appointment.query.all()
    return render_template('schedule.html', appointments=appointments)

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    time = request.form.get('time')
    if name and time:
        try:
            new_appointment = Appointment(name=name, time=time)
            db.session.add(new_appointment)
            db.session.commit()
            logging.info(f"Appointment booked for {name} at {time}.")
        except Exception as e:
            db.session.rollback()  # Rollback in case of failure
            logging.error(f"Failed to book appointment: {e}")
    return redirect(url_for('home'))

# Route to check that appointments are being saved in the SQLite Database
@app.route('/appointments', methods=['GET'])
def view_appointments():
    appointments = Appointment.query.all()
    return jsonify([{'name': appt.name, 'time': appt.time} for appt in appointments])

from flask import request, jsonify
from models import db, Schedule

@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    data = request.get_json()
    new_schedule = Schedule(user_id=data['user_id'], event=data['event'], date=data['date'])
    db.session.add(new_schedule)
    db.session.commit()
    return jsonify({'message': 'Schedule added successfully!'}), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
