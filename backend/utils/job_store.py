from database import get_connection


def create_job(job_id):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO jobs (
            id,
            status
        )
        VALUES (?, ?)
        """,
        (
            job_id,
            "processing"
        )
    )

    conn.commit()

    conn.close()


def complete_job(
    job_id,
    download_url,
    output_filename
):

    conn = get_connection()

    conn.execute(
        """
        UPDATE jobs
        SET
            status=?,
            download_url=?,
            output_filename=?
        WHERE id=?
        """,
        (
            "completed",
            download_url,
            output_filename,
            job_id
        )
    )

    conn.commit()

    conn.close()


def fail_job(
    job_id,
    error
):

    conn = get_connection()

    conn.execute(
        """
        UPDATE jobs
        SET
            status=?,
            error=?
        WHERE id=?
        """,
        (
            "failed",
            str(error),
            job_id
        )
    )

    conn.commit()

    conn.close()


def get_job(job_id):

    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM jobs
        WHERE id=?
        """,
        (job_id,)
    ).fetchone()

    conn.close()

    if row is None:
        return None

    return dict(row)