from flask import Blueprint, request, send_file, jsonify

from services.pdf_services import split_pdf

from utils.file_handler import (
    save_file,
    create_job_folder,
    generate_output_path
)

from utils.zip_handler import create_zip

from utils.validators import (
    validate_pdf,
    validate_pdf_content
)

from utils.job_store import (
    create_job,
    complete_job,
    fail_job
)


split_bp = Blueprint("split", __name__)


@split_bp.route("/", methods=["POST"])
def split_route():

    try:

        file = request.files["file"]
        validate_pdf(file)

        split_after = request.form[
            "split_after"
        ]

        split_points = [
            int(x.strip())
            for x in split_after.split(",")
        ]

        input_path = save_file(file)
        validate_pdf_content(input_path)

        job_id, job_folder = create_job_folder()
        create_job(job_id)

        split_files = split_pdf(
            input_path,
            split_points,
            job_folder
        )

        zip_path = generate_output_path(
            job_folder,
            "split_result.zip"
        )

        create_zip(
            split_files,
            zip_path
        )

        download_url = f"/download/{job_id}"

        complete_job(
            job_id,
            download_url,
            "split_result.zip"
        )

        return jsonify({

            "job_id": job_id,

            "status": "completed",

            "download_url": download_url
        })

    except Exception as e:

        if "job_id" in locals():

            fail_job(job_id, e)

        return jsonify({
            "error": str(e)
        }), 500