from database import get_connection

conn = get_connection()

conn.execute(
    """
    DELETE FROM jobs
    WHERE created_at <
    datetime(
        'now',
        '-7 days'
    )
    """
)

conn.commit()

conn.close()

print("Old jobs removed")