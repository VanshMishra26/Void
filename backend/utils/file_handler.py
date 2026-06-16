import os
import uuid
import shutil

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def create_job_folder():

    job_id = str(uuid.uuid4())

    job_path = os.path.join(
        OUTPUT_FOLDER,
        job_id
    )

    os.makedirs(job_path, exist_ok=True)

    return job_id, job_path


def save_file(file):

    ext = file.filename.split('.')[-1]

    filename = f"{uuid.uuid4()}.{ext}"

    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(path)

    return path


def generate_output_path(
    folder,
    filename
):

    return os.path.join(folder, filename)


def cleanup_job_folder(job_path):

    if os.path.exists(job_path):
        shutil.rmtree(job_path)