# Cloud Project 1: S3 File Uploader — Professional Guide

## Goal
Make this project look like real production work — not a tutorial exercise.

---

## Repo Structure
```
s3-file-uploader/
├── uploader/
│   ├── __init__.py
│   └── s3_client.py       # core upload logic
├── main.py                # CLI entry point
├── requirements.txt       # boto3
├── .env.example           # AWS_BUCKET_NAME, AWS_REGION (never commit .env)
├── .gitignore             # include .env, __pycache__, *.pyc
└── README.md
```

---

## README.md Structure (most important)
```
# S3 File Uploader

A CLI tool to upload files to AWS S3 with error handling and URI confirmation.

## Features
- Validates local file existence before upload
- Handles AWS ClientError gracefully
- Prints S3 URI on success

## Setup
1. Clone the repo
2. pip install -r requirements.txt
3. aws configure (or set credentials in .env)

## Usage
python main.py

## Tech Stack
- Python 3.12
- Boto3 (AWS SDK)
- AWS S3
```

---

## What Makes It Resume-Ready

### 1. Commit History Tells a Story
Don't make one giant commit. Break it into:
- `init: project structure and dependencies`
- `feat: add s3 upload function with error handling`
- `feat: add CLI entry point with user input`
- `fix: handle missing file path gracefully`
- `docs: add README with setup and usage`

### 2. .gitignore Non-Negotiables
```
.env
__pycache__/
*.pyc
*.pyo
.DS_Store
```

### 3. requirements.txt
```
boto3==1.34.0
```
Pin the version — it signals professionalism.

### 4. Never Hardcode Credentials
Use environment variables:
```python
import os
bucket = os.environ.get("AWS_BUCKET_NAME")
```

---

## How to Present It on Resume
```
S3 File Uploader | Python, Boto3, AWS S3
- Built a CLI tool to upload files to S3 with input validation and error handling
- Structured as a reusable Python package following PEP 8 and type hint standards
- GitHub: github.com/yourhandle/s3-file-uploader
```

One line per impact. No filler words.

---

## Stretch Goals (makes it stand out more)
- Add `--recursive` flag to upload entire folders
- Add progress bar using `tqdm`
- Add `--dry-run` flag to preview without uploading
- Write one unit test using `moto` (AWS mock library)
