import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="sqlguy7",
    database="posted_data" # database where users can post their data
)

cursor = db.cursor()

def execute(sql,values=None):
    cursor.execute(sql,values)
    db.commit()

def executemany(sql,values=None):
    cursor.executemany(sql,values)
    db.commit()

def cm(sql):
    cursor.execute(sql)

def getDict(table):
    dc = db.cursor(dictionary=True)
    dc.execute("SELECT * FROM " + table)
    return dc.fetchall()

def post(text,username):
    execute("INSERT INTO post_data (data,username) VALUES (%s,'%s')" % (text,username))

def get(username):
    # select * from post_data where username = %s
    cm("SELECT * FROM post_data WHERE username = '%s'" % (username,))
    return cursor.fetchall()

def fetch(sql,values=None):
    cursor.execute(sql,values)
    return cursor.fetchall()

def clear(username):
    execute("DELETE FROM post_data WHERE username = '%s'" % (username,))