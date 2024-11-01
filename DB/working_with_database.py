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
    
def all_task_db():
    connect = sqlite3.connect('affairs.db')
    cursor = connect.cursor()
    
    cursor.execute("SELECT * FROM to_do_list")
    result = cursor.fetchall()
    
    connect.close()
    
    return result

def add_db(pr : int, tx : str):
    connect = sqlite3.connect('affairs.db')
    cursor = connect.cursor()
    
    cursor.execute("INSERT INTO to_do_list (priority, name) VALUES (?, ?)", (pr, tx))
    
    connect.commit()
    connect.close()
    
def del_db(id_):
    connect = sqlite3.connect('affairs.db')
    cursor = connect.cursor()
    
    cursor.execute("DELETE FROM to_do_list WHERE id = ?", (id_,))
    
    connect.commit()
    connect.close()