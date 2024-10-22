-------------------------------------------------------------------------
# Scheduling Utility #

## Overview
The Scheduling Utility is a simple web application built with Flask 
that allows users to book appointments. It provides a user-friendly 
interface for scheduling and viewing appointments.

## Features
- Book appointments with user name and time. - View all booked 
appointments. - Persistent storage using SQLite (or any database 
specified).

# Getting Started #

## Prerequisites
- Python 3.x - pip (Python package installer)

## Installation
1. **Clone the Repository**: ```bash git clone <repository-url> cd 
   scheduling_app

-------------------------------------------------------------------------

# Install Dependencies: #
 
 - pip install -r requirements.txt
 # If you run into any issue with installing lxml 
 # (especially when using Termux, you can just make sure 
 # you have the following packages installed: `libxml2 
 # libxslt clang`. Command => "pkg install libxml2 libxslt clang"


# Set Up Environment Variables: Create a .env file in the project directory and add: 
 
 - FLASK_ENV=development 
 # Change to production for live environment 
 
 - DATABASE_URL=sqlite:///appointments.db 
 # Use your actual database URI if needed

-------------------------------------------------------------------------

# Running the Application #

# Start the application by running:
 - python app.py 
# The app will be accessible at http://127.0.0.1:5000.

# Deployment #
 - For deployment, consider using services like Railway, Render, or 
Heroku. Follow their specific instructions for deployment.

# Contributing #
 - Contributions are welcome! Please submit a pull request or open an 
issue for any feature requests or bugs.

# License #
 - This project is licensed under the MIT License. See the LICENSE file 
for details.
-------------------------------------------------------------------------
