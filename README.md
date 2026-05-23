# ResumeTweaker
Initial Steps to consider:
1. UI for File upload and Job Description input Field
2. Implement a Document Parser supporting both pdf and word docx as valid files.
3. Use NLP library to extract key terms and keywords from uploaded resume.
4. Repeat Step 3 for Job Description pasted.
5. Edit uploaded resume to tweak current resume only rephrasing current projects and experiences to include missing keywords from Job Descriptions.
6. Compile and Export edited resume into respective pdf or docx formats.


## Architectural Decisions & Research

* **Layout Ingestion (PyMuPDF):** Standard parsers merge text horizontally across the page, breaking multi-column resume layouts. This project utilizes PyMuPDF (`fitz`) to extract block coordinates, enabling vertical-first block sorting to preserve column reading integrity.
* **Semantic Analysis (TensorFlow Hub + KeyBERT):** Bypasses standard keyword counting by utilizing contextual embeddings to calculate cosine similarity scores between phrases. Integrating a TF Hub layer helps filter corporate filler text to isolate true engineering requirements.
* **Decoupled LLM Pipeline (Claude API):** Rejects the "one giant prompt" approach. Local scripts extract data and map gaps, while the external generative model is restricted strictly to editing project achievements—maximizing accuracy while protecting personal PII data.
