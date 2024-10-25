import os
import logging
from flask import Flask, request, render_template, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db

app = Flask(__name__)

# Use environment variable for the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

load_dotenv()
# Create the database tables
with app.app_context():
    db.create_all()  # Creates tables if they don't exist

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log an event when the app starts
@app.before_first_request
def setup_logging():
    logger.info("Starting the scheduling app")

# In routes, use logger to capture specific events
@app.route('/book', methods=['POST'])
def book():
    try:
        # booking logic here
        db.session.commit()
        flash("Booking successful", "success")
        logger.info("Booking completed successfully")
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while booking", "error")
        logger.error(f"Booking failed: {e}")
    return redirect(url_for('home'))


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
