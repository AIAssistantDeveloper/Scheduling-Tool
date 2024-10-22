from datetime import datetime
from app import db

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False)  # Better to store as DateTime
    created_at = db.Column(db.DateTime, default=datetime.utcnow)