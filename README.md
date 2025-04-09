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

## How It Works

### 1. Using OpenAI API for Resume Evaluation

This application integrates the OpenAI API to perform natural language reasoning on resumes. Specifically, it sends both the resume text and the job description to a prompt defined in `ai_logic.py`. This prompt instructs the language model (gpt-3.5-turbo) to summarize the resume and provide a clear explanation of whether the candidate is a good fit for the role.

### 2. Match Scoring with Cosine Similarity 

The app uses **cosine similarity** to compute how closely a resume matches a given job description. This approach enables semantic matching rather than simple keyword overlap, allowing for a more accurate and meaningful comparison.

Cosine similarity is a metric used to measure the similarity between two non-zero vectors in a multi-dimensional space. In the context of Natural Language Processing (NLP), we convert text data (e.g., resumes and job descriptions) into vector embeddings using a pre-trained language model like 'SentenceTransformers'. Once both texts are represented as vectors, cosine similarity quantifies the angle between them:

**cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)**


Where:
- \( A \) and \( B \) are embedding vectors
- (A · B) is the dot product
- ||A|| and ||B|| are magnitudes (Euclidean norms)

The result is a score between **-1 and 1**:
- **1**: Perfectly similar
- **0**: No similarity
- **-1**: Perfectly opposite (rare in practice for this use case)

## Setup
### 1. Clone the repo
```bash
git clone https://github.com/lizardcat/ai-resume-filter-v2.git
cd ai-resume-filter-v2
```

### 2. Create a virtual environment in the project root (Optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install dependencies
Install all required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 4. In the project root, create a file called `.env` and add your OpenAI API key ([GET ONE HERE](https://platform.openai.com)):

```
OPENAI_API_KEY=your-openai-key-here
```
Replace `your-openai-key-here` with your actual OpenAI API key (e.g., sk-...).

    Note: The .env file is used to store sensitive credentials and should not be committed to version control. It is typically included in .gitignore to keep your API keys private.

### 4. Run the app:

```bash
python app.py
```

Then go to [http://localhost:5000](http://localhost:5000) in your browser.

## Screenshots
### 1. Resume Upload & Job Description Page
![Page for entering job description and resumes for processing](assets/ai-resume-filter-1.png)

### 2. Screening Results with Summary from AI and Score Based on Cosine Similarity
![Page showing screening score and summary output from AI](assets/ai-resume-filter-2.png)