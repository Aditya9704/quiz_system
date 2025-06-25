import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT,
            option_b TEXT,
            option_c TEXT,
            option_d TEXT,
            correct_option TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database and table created successfully.")

if __name__ == "__main__":
    create_database()
