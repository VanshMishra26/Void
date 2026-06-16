from flask import Blueprint, jsonify

from utils.job_store import get_job

jobs_bp = Blueprint(
    "jobs",
    __name__
)


@jobs_bp.route("/<job_id>")
def job_status(job_id):

    job = get_job(job_id)

    if not job:

        return jsonify({
            "error": "Job not found"
        }), 404

    return jsonify(job)