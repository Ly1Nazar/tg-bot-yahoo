import sqlite3

def create_db():
    con = sqlite3.connect('history.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE requests
                   (date text, chat_id text, message_text text)''')

    con.commit()
    con.close()