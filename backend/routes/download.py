from flask import Blueprint
from flask import send_file
from flask import jsonify

import os

from utils.job_store import get_job

download_bp = Blueprint(
    "download",
    __name__
)


@download_bp.route("/<job_id>")
def download(job_id):

    job = get_job(job_id)

    if not job:

        return jsonify({
            "error": "Job not found"
        }), 404

    filename = job["output_filename"]

    output_file = os.path.join(
        "outputs",
        job_id,
        filename
    )

    if not os.path.exists(output_file):

        return jsonify({
            "error": "Output file missing"
        }), 404

    return send_file(
        output_file,
        as_attachment=True
    )