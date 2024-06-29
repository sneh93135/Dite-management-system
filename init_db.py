from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db  # Assuming your app and db are defined in app.py

# Ensure app context is pushed
app.app_context().push()

# Create tables
db.create_all()
print("Database and tables created")
