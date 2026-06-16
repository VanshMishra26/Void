from database import get_connection

conn = get_connection()

conn.execute("""
CREATE TABLE IF NOT EXISTS jobs (

    id TEXT PRIMARY KEY,

    status TEXT NOT NULL,

    download_url TEXT,

    output_filename TEXT,

    error TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

conn.close()

print("Database initialized")