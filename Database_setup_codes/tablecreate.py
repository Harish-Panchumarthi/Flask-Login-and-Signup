import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    #cursorObj.execute("CREATE TABLE login( id INTEGER PRIMARY KEY,uname TEXT,pwd TEXT)")
    
    cursorObj.execute("CREATE TABLE signup( id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,email TEXT,pwd TEXT,pwdr TEXT)")

    con.commit()

con = sql_connection()

sql_table(con)