import sqlite3

def end_message():
    print("Program done!")
    return True

def connection_db():
    try:
        conn = sqlite3.connect("user.db")
        #cursor = connection.cursor()
        conn.execute("CREATE TABLE users(id INTEGER NOT NULL UNIQUE, name TEXT NOT NULL, password TEXT NOT NULL, description TEXT, PRIMARY KEY(id AUTOINCREMENT));")
        conn.close()
        return True
    except sqlite3.OperationalError:
        return False

def insert_db(name, password, description=""):
    conn = sqlite3.connect("user.db")
    conn.execute(f"INSERT INTO users(name, password, description) VALUES ('{name}', '{password}', '{description}');")
    conn.commit()
    conn.close()
    return True

def select_db(name, password):
    account = ()
    conn = sqlite3.connect("user.db")
    cursor = conn.execute(f"SELECT * FROM users WHERE name='{name}' AND password='{password}';")
    for i in cursor:
        account = i 
    conn.close()
    return account

def delete_db(name, password):
    conn = sqlite3.connect("user.db")
    conn.execute(f"DELETE FROM users WHERE name='{name}' AND password='{password}';")
    conn.commit()
    conn.close()
    return True
