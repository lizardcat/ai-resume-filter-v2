from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ResumeReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_text = db.Column(db.Text, nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
