# ResumeTweaker

> An AI-powered resume tailoring pipeline that analyzes your resume against a job description, identifies keyword gaps, and rephrases your project bullets to close them — without sending your personal data to an external model.

**Status:** Active development · Architecture designed · Implementation in progress

---

## What it does

Most resume tailoring tools either do a naive keyword count or dump your entire resume into a single LLM prompt. ResumeTweaker does neither.

1. **Parses** uploaded PDF or DOCX resumes while preserving multi-column layout integrity
2. **Extracts** keywords from both your resume and the target job description using semantic NLP (TF-IDF → KeyBERT → contextual embeddings)
3. **Identifies** the gap — skills and phrases in the JD that are missing or underrepresented in your resume
4. **Rephrases** only your project and experience bullets using an LLM, scoped strictly to rewriting — no raw personal data sent to the model
5. **Exports** the tailored resume back to PDF or DOCX format

---

## Architecture decisions

### Layout Ingestion — PyMuPDF (`fitz`)
Standard text parsers merge content horizontally across the page, completely breaking multi-column resume layouts. ResumeTweaker uses PyMuPDF to extract block coordinates and sorts them vertically-first, preserving column reading order and structural integrity.

### Keyword Extraction — TF-IDF → KeyBERT
Started with TF-IDF for baseline frequency analysis, then layered in KeyBERT with TensorFlow Hub contextual embeddings to compute cosine similarity scores between resume phrases and JD requirements. This moves beyond keyword counting to semantic relevance — filtering corporate filler to isolate true engineering signals.

### Decoupled LLM Pipeline — Claude API
Rejects the "one giant prompt" approach. Local scripts handle all parsing, extraction, and gap mapping. The Claude API (OpenAI-compatible) is called only for the rewrite step — restricted strictly to rephrasing project achievements. This keeps PII local and maximises edit precision.

---

## Tech stack

| Layer | Technology |
|---|---|
| Document Parsing | PyMuPDF (fitz), python-docx |
| Keyword Extraction | TF-IDF, KeyBERT, TensorFlow Hub |
| LLM Integration | Claude API (Anthropic) |
| Backend API | FastAPI |
| Frontend | Flask, JavaScript |
| Language | Python 3.10+ |

---

## Project structure (planned)

```
ResumeTweaker/
├── parser/           # PDF and DOCX ingestion + block sorting (PyMuPDF)
├── extractor/        # TF-IDF and KeyBERT keyword extraction
├── gap_analysis/     # Resume vs JD comparison and scoring
├── llm_pipeline/     # Claude API rewrite module (decoupled)
├── exporter/         # PDF and DOCX output generation
├── api/              # FastAPI endpoints
└── frontend/         # Flask UI for file upload and output preview
```

> Two architectural branches are currently scaffolded: one Flask-based, one FastAPI-based. Final stack decision pending implementation benchmarking.

---

## Getting started

```bash
# Clone the repo
git clone https://github.com/Saumy-m/ResumeTweaker.git
cd ResumeTweaker

# Install dependencies
pip install -r requirements.txt

# Add your API key
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# Run the app
uvicorn api.main:app --reload
```

Then open `http://localhost:8000` in your browser.

---

## Roadmap

- [x] Architectural research — PyMuPDF layout ingestion, KeyBERT semantic analysis, decoupled LLM pipeline
- [x] Dual-branch architecture scaffolded (Flask branch + FastAPI branch)
- [x] KeyBERT validated on real LinkedIn job descriptions via Google Colab prototype
- [ ] PDF and DOCX parser with vertical-first block sorting (PyMuPDF)
- [ ] TF-IDF keyword extraction baseline
- [ ] KeyBERT + TensorFlow Hub semantic similarity layer
- [ ] Gap analysis scoring and ranking (resume vs JD delta)
- [ ] Claude API rewrite pipeline (decoupled, PII-safe)
- [ ] DOCX export with original formatting preserved
- [ ] PDF export
- [ ] Frontend UI (file upload + JD input + diff preview)
- [ ] End-to-end integration and testing

---

## Why I built this

I kept noticing that tailoring a resume to a job description took 30–45 minutes of manual work per application — and most of that was repetitive keyword matching and bullet rephrasing. I wanted a tool that did the mechanical part intelligently, leaving me to review and approve rather than write from scratch.

The interesting engineering problem turned out to be the parsing layer: preserving multi-column resume layouts is harder than it sounds, and most off-the-shelf solutions fail on real resumes. The semantic gap analysis layer — moving from frequency counting to actual contextual similarity — was the other rabbit hole worth going down.

---

## Author

**Saumya Mehta** · [linkedin.com/in/saumya-mehta06](https://linkedin.com/in/saumya-mehta06) · [github.com/Saumy-m](https://github.com/Saumy-m)