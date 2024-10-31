import sqlite3

def connect():
    connect = sqlite3.connect('affairs.db')
    cursor = connect.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS to_do_list (
    id INTEGER PRIMARY KEY,
    priority INTEGER,
    name TEXT NOT NULL
    )
    """)
    
    connect.close()
    
def all_task():
    connect = sqlite3.connect('affairs.db')
    cursor = connect.cursor()
    
    cursor.execute("SELECT * FROM to_do_list")
    result = cursor.fetchall()
    
    connect.close()
    
    return result