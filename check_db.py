import sqlite3
import arrow

con = sqlite3.connect('history.db')
cur = con.cursor()
now = arrow.now()

cur.execute("INSERT INTO requests VALUES (?, ?, ?)", (now.format('DD-MM-YYYY HH:mm'), 595394554, "text"))
for row in cur.execute('SELECT * FROM requests'):
    print(str(row))


con.commit()
con.close()
