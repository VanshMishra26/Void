# Void PDF Toolkit

A modular PDF processing backend inspired by Smallpdf and ILovePDF.

## Features

### PDF Operations

- Merge PDFs
- Split PDFs
- Compress PDFs

### Validation

- PDF type validation
- Corrupted PDF detection
- Encrypted PDF detection
- 100 MB file size limit

### Job System

- SQLite persistence
- Job tracking
- Download endpoints
- Cleanup utilities

## API Endpoints

### Merge PDFs

POST /merge

### Split PDFs

POST /split

### Compress PDFs

POST /compress

### Download Result

GET /download/<job_id>

### Job Status

GET /jobs/<job_id>

## Tech Stack

- Python
- Flask
- SQLite
- PyPDF2
- PyMuPDF

## Roadmap

### Version 1.1

- Image → PDF
- PDF → Image
- DOCX → PDF
- PDF → DOCX

### Version 2.0

- React Frontend
- Authentication
- Redis
- Celery
- AWS S3