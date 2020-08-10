import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()
    a=input('enter')
    cursorObj.execute('select email from signup')
    
    #cursorObj.execute('select grade from students where grade <84')
    rows = cursorObj.fetchall()
    print(rows)
    if(a==db.email){
      print('Success')
    }
    else{
      print('Failed')
    }

sql_fetch(con)
