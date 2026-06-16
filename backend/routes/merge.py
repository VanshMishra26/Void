from flask import Blueprint, request, jsonify
import os
from services.pdf_services import merge_pdfs
from utils.file_handler import(create_job_folder, save_file, generate_output_path)
from utils.validators import (
    validate_pdf,
    validate_pdf_content
)
from utils.job_store import (
    create_job,
    complete_job,
    fail_job
)
from utils.logger import logger

merge_bp = Blueprint("merge", __name__)

@merge_bp.route("/", methods=["POST"])
def merge_route():

    try:
        files = request.files.getlist("files")
        logger.info(
            f"Merge request received | Files: {len(files)}"
        )
        
        if len(files) < 2:
            return jsonify({
                "error": "Upload at least 2 PDFs"
            }), 400

        # Validation
        for file in files:
            validate_pdf(file)

        job_id, job_folder = create_job_folder()
        create_job(job_id)
        logger.info(
           f"Merge job created : {job_id}" 
        )

        # Save files
        paths = []
        for file in files:
            path = save_file(file)
            validate_pdf_content(path)
            paths.append(path)

        output = generate_output_path(job_folder, "merged.pdf")
        logger.info(
            f"Output path: {output}"
        )
        merge_pdfs(paths,output)
        size = os.path.getsize(output)
        logger.info(
            f"Merge complete: {job_id} | Size: {size} bytes"
        )

        download_url = f"/download/{job_id}"

        complete_job(job_id,download_url,"merged.pdf")

        return jsonify({
            "job_id": job_id, "status": "completed","download_url": download_url
        })

    except Exception as e:
        if "job_id" in locals():

            fail_job(
                job_id,
                e
            )

            logger.exception(
                f"Merge failed: {job_id}"
            )

        return jsonify({
            "error": str(e)
        }), 500