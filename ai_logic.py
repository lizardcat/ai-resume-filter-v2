from sentence_transformers import SentenceTransformer, util
import openai
import os
from models import ResumeReview, db

embedder = SentenceTransformer('all-MiniLM-L6-v2')
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment

def compute_match_score(resume_text, job_description):
    resume_embedding = embedder.encode(resume_text, convert_to_tensor=True)
    job_embedding = embedder.encode(job_description, convert_to_tensor=True)
    score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    return score

def generate_reasoning(resume_text, job_description):
    prompt = f"""
You are an AI HR assistant. Given the following job description and resume, determine how well the resume fits the job and explain why.

Job Description:
{job_description}

Resume:
{resume_text}

Respond with a clear summary of how well this candidate fits the role and list key points for the decision. Please include the name of the candidate at the beginning before your summary.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response['choices'][0]['message']['content']

def save_review(resume, job, score, explanation):
    review = ResumeReview(
        resume_text=resume,
        job_description=job,
        score=score,
        explanation=explanation
    )
    db.session.add(review)
    db.session.commit()
