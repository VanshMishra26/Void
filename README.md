# Void

> A modular document processing backend inspired by tools like Smallpdf and ILovePDF.

Void is a scalable PDF processing platform built with Flask and Python. It provides APIs for merging, splitting, and compressing PDF files while maintaining a clean, extensible architecture that can support future document conversion features.

---

## Features

### PDF Operations

* Merge multiple PDFs into a single document
* Split PDFs using custom page break points
* Compress PDF files using PyMuPDF

### Validation Layer

* PDF file type validation
* Corrupted PDF detection
* Encrypted PDF detection
* Configurable file size limits (currently 100 MB)

### Job-Based Processing

* Unique Job IDs
* Job status tracking
* Download endpoints
* Output file management

### Persistence

* SQLite-backed job storage
* Persistent job metadata
* Download URL tracking

### Logging

* Centralized application logging
* Request lifecycle tracking
* Error logging and debugging support

### Maintenance Utilities

* Automatic cleanup utilities
* Old job cleanup scripts
* Output directory management

---

## Project Structure

```text
Void/
│
├── backend/
│   │
│   ├── routes/
│   │   ├── merge.py
│   │   ├── split.py
│   │   ├── compress.py
│   │   ├── download.py
│   │   └── jobs.py
│   │
│   ├── services/
│   │   ├── pdf_services.py
│   │   └── compression/
│   │
│   ├── utils/
│   │
│   ├── app.py
│   ├── database.py
│   ├── init_db.py
│   ├── cleanup.py
│   └── cleanup_jobs.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## API Endpoints

### Merge PDFs

```http
POST /merge
```

Merge multiple PDF files into a single document.

---

### Split PDF

```http
POST /split
```

Split a PDF using one or more page break points.

Example:

```text
split_after=2,5
```

Result:

```text
Pages 1-2
Pages 3-5
Pages 6-end
```

---

### Compress PDF

```http
POST /compress
```

Compress a PDF while preserving readability.

Current Engine:

* PyMuPDF

Future Engine:

* Ghostscript

---

### Download Result

```http
GET /download/<job_id>
```

Download generated files.

---

### Job Status

```http
GET /jobs/<job_id>
```

Retrieve current job status.

Example Response:

```json
{
    "status": "completed",
    "download_url": "/download/<job_id>"
}
```

---

## Technology Stack

### Backend

* Python
* Flask

### PDF Processing

* PyPDF2
* PyMuPDF

### Database

* SQLite

### Logging

* Python Logging

---

## Installation

Clone the repository:

```bash
git clone https://github.com/VanshMishra26/Void.git
cd Void
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the database:

```bash
python backend/init_db.py
```

Start the server:

```bash
python backend/app.py
```

---

## Example Usage

Merge PDFs:

```bash
curl.exe -X POST http://127.0.0.1:5000/merge/ ^
-F "files=@file1.pdf" ^
-F "files=@file2.pdf"
```

Compress PDF:

```bash
curl.exe -X POST http://127.0.0.1:5000/compress/ ^
-F "file=@document.pdf"
```

---

## Roadmap

### Version 1.1

* Image → PDF
* PDF → Image
* DOCX → PDF
* PDF → DOCX

### Version 1.2

* Batch Processing
* Advanced Compression Profiles
* Async Background Jobs

### Version 2.0

* React Frontend
* User Authentication
* Cloud Storage Integration
* Docker Deployment
* Redis + Celery
* AWS S3 Support

---

## Design Principles

Void is built around:

* Modularity
* Scalability
* Maintainability
* Extensibility

The architecture is designed so that new processing engines and document conversion workflows can be added with minimal changes to the existing codebase.

---

## Version

Current Release:

```text
v1.0.0
```

---

## Author

**Vansh Mishra**

GitHub:
https://github.com/VanshMishra26
