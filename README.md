# AI Resume Screener

This is an AI-powered resume screening system built using Python, Flask, and SQLite. It uses OpenAI's language models and Sentence Transformers to semantically compare uploaded resumes against a given job description, calculate a match score, and generate a natural language explanation for the match.

## Features
- Upload one or more resumes in PDF or DOCX format
- Enter a job description to compare against
- Automatically scores each resume based on semantic similarity
- Generates explanations for match quality using AI
- Stores all results in a local SQLite database
- Filter results by match score threshold
- Simple Bootstrap-based responsive UI

## Requirements
- Python 3.9+

### Python Dependencies
Install all required dependencies using pip:

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install flask flask_sqlalchemy sentence-transformers openai python-docx pymupdf python-dotenv
```

## Setup
1. Clone the repo
2. In the project root, create a file called `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your-openai-key-here
```

3. Run the app:

```bash
python app.py
```

Then go to [http://localhost:5000](http://localhost:5000) in your browser.

## Notes
- Uploaded files are saved to the `uploads/` folder.
- Resume match results are stored in `reviews.db`.
- The `.env` file is ignored via `.gitignore` — do not commit your API key.
