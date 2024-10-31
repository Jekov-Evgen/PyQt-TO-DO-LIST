import sqlite3

def connect():
    connect = sqlite3.connect('affairs.db')
    cursor = connect.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS to_do_list (
    priority INTEGER
    name TEXT NOT NULL
    )
    """)
    
    connect.close()