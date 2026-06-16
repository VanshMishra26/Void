import os

from PyPDF2 import PdfReader


ALLOWED_EXTENSIONS = {".pdf"}

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB


def validate_pdf(file):

    # extension check
    ext = os.path.splitext(
        file.filename
    )[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Only PDF files are allowed"
        )

    # size check
    file.seek(0, os.SEEK_END)

    size = file.tell()

    file.seek(0)

    if size > MAX_FILE_SIZE:
        raise ValueError(
            "File exceeds 100MB limit"
        )


def validate_pdf_content(path):

    try:

        reader = PdfReader(path)

        # encrypted PDF check
        if reader.is_encrypted:
            raise ValueError(
                "Encrypted PDFs are not supported"
            )

        # malformed PDF check
        _ = len(reader.pages)

    except Exception:
        raise ValueError(
            "Invalid or corrupted PDF"
        )