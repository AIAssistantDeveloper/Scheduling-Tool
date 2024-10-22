import os
import logging
from flask import Flask, request, render_template, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from a .env file
load_dotenv()

# Configure the SQLAlchemy database URI (adjust this to your database)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///appointments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"An error occurred: {e}")
    return "An internal error occurred.", 500

# Home route to display appointments
@app.route('/')
def home():
    appointments = Appointment.query.all()
    return render_template('schedule.html', appointments=appointments)

# Route to book an appointment
@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    time = request.form.get('time')
    if name and time:
        new_appointment = Appointment(name=name, time=time)
        db.session.add(new_appointment)
        db.session.commit()
    return redirect(url_for('home'))

# Route to check that appointments are being saved in the SQLite Database
@app.route('/appointments', methods=['GET'])
def view_appointments():
    appointments = Appointment.query.all()
    return jsonify([{'name': appt.name, 'time': appt.time} for appt in appointments])

# Run the app
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
