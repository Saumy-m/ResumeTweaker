# Imports go here
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import os
import python_multipart

# Initialize the FastAPI instance
app = FastAPI()

# Initialize the Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define a route for the home page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"status": "Success"})

# Define a route to handle form submission
@app.post("/", response_class=HTMLResponse)
async def submit_form(request: Request, job_descript: str = Form(...), file_Input: UploadFile = File(...)):
    # Process the uploaded file (for demonstration, we just read its content)
    file_content = await file_Input.read()
    
    print("\n--- FASTAPI LOGS ---")
    print(f"Captured text length: {len(job_descript)} chars")
    print(f"Captured file name: {file_Input.filename}")
    print("--------------------\n")

    return "Form submitted successfully!"