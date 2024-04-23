import psycopg2 as ps

conn = ps.connect(host = 'localhost',
                  dbname = 'Wentil2right',
                  user = 'Wentil2right',
                  password = '2006',
                  port = '5432'
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE snake (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL
);
""")


conn.commit()

cur.close()
conn.close()