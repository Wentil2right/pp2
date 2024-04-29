import psycopg2 as ps

conn = ps.connect(host = 'localhost',
                  dbname = 'Snake',
                  user = 'Bolat',
                  password = 'Bolat_2005',
                  port = '3306'
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