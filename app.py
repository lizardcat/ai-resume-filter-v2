from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from models import db, ResumeReview
from parser import extract_resume_text
from ai_logic import compute_match_score, generate_reasoning, save_review

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('resumeFiles')  # get all uploaded files
        job = request.form['job']

        for file in files:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            resume_text = extract_resume_text(file_path)
            if not resume_text:
                continue  # skip invalid files

            score = compute_match_score(resume_text, job)
            explanation = generate_reasoning(resume_text, job)
            save_review(resume_text, job, score, explanation)

        return redirect(url_for('results'))
    return render_template('index.html')


@app.route('/results')
def results():
    min_score = request.args.get('min_score', type=float)
    query = ResumeReview.query
    if min_score is not None:
        query = query.filter(ResumeReview.score >= min_score)
    reviews = query.order_by(ResumeReview.score.desc()).all()
    return render_template('results.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
