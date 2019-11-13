from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
   

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
db = SQLAlchemy(app)

class Report(db.Model):
    incident_id = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.String(100), nullable = False)
    incident_type = db.Column(db.String(100), nullable = False)
    incident_priority = db.Column(db.String(100), nullable = False)
    incident_description = db.Column(db.String(500), nullable = False)
    incident_image = db.Column() # use image_attach API 

    incident_date = db.Column(db.DateTime, nullable = False)
    incident_time = db.Column(db.String, nullable = False)
    incident_address = db.Column(db.String(200), nullable = False)
    incident_city = db.Column(db.String(100), nullable = False)
    incident_state = db.Column(db.String(100), nullable = False)
    incident_country = db.Column(db.String(200), nullable = False)
    
    user_name = db.Column(db.String(200), default = "anon", nullable = False)
    user_phone = db.Column(db.Integer)
    user_mail = db.Column(db.String(200))
    user_address = db.Column(db.String(200))

    assigned_to = db.Column(db.String(200), default = "Not assigned yet")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port = "5001")