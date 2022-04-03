import sqlite3 as sql
from os import path
   
root = path.dirname(path.relpath((__file__)))
   
def create_post(name, address):
    con = sql.connect(path.join(root, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into alemtbl (name, address) values(?,?)', (name, address))
    con.commit()
    con.close()
   
def get_posts():
    con = sql.connect(path.join(root, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from alemtbl')
    posts = cur.fetchall()
    return posts 
