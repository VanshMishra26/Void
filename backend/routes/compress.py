from flask import Blueprint
from flask import request
from flask import jsonify

from utils.validators import (
    validate_pdf,
    validate_pdf_content
)

from utils.file_handler import (
    save_file,
    create_job_folder,
    generate_output_path
)

from utils.job_store import (
    create_job,
    complete_job,
    fail_job
)

from services.compression.compressor import (
    compress_pdf
)

compress_bp = Blueprint(
    "compress",
    __name__
)

@compress_bp.route("/", methods=["POST"])
def compress_route():

    try:

        file = request.files["file"]

        validate_pdf(file)

        input_path = save_file(file)

        validate_pdf_content(input_path)

        job_id, job_folder = create_job_folder()

        create_job(job_id)

        output_path = generate_output_path(
            job_folder,
            "compressed.pdf"
        )

        compress_pdf(
            input_path,
            output_path
        )

        download_url = (
            f"/download/{job_id}"
        )

        complete_job(
            job_id,
            download_url,
            "compressed.pdf"
        )

        return jsonify({

            "job_id": job_id,

            "status": "completed",

            "download_url": download_url

        })

    except Exception as e:

        if "job_id" in locals():

            fail_job(
                job_id,
                e
            )

        return jsonify({
            "error": str(e)
        }), 500