from flask import Flask, render_template, request
import sqlite3
app=Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')
@app.route('/ind')
def ind():
    return render_template('signup.html')
@app.route('/hell',methods = ['POST', 'GET'])
def hell():
   if request.method == 'POST':

         
         con = sqlite3.connect('mydatabase.db')
         uname = request.form['uname']
         pwd = request.form['pwd']
         cursorObj = con.cursor()
         cur = con.cursor()
         cursorObj = con.cursor()
         login=cursorObj.execute("SELECT * FROM signup WHERE email= ? and pwd= ?;",(uname,pwd))
         con.commit()
         if (len(login.fetchall()) > 0):
                   return render_template("secret.html")
         else:
                   return render_template("login.html")
@app.route('/gol',methods = ['POST', 'GET'])
def gol():
   if request.method == 'POST':
         con = sqlite3.connect('mydatabase.db')

         
         fname = request.form['fname']
         lname = request.form['lname']
         email = request.form['email']
         pwd = request.form['pwd']
         pwdr = request.form['pwdr']
         cursorObj = con.cursor()
         cursorObj = con.cursor()
         login=cursorObj.execute("SELECT * FROM signup WHERE email= ?;",(email,))
         con.commit()
         if (len(login.fetchall()) > 0):
                   return render_template("signup.html")
         else:
                   cursorObj.execute("INSERT INTO signup(fname,lname,email,pwd,pwdr) VALUES('"+fname+"','"+lname+"','"+email+"','"+pwd+"','"+pwdr+"')")
             
                   con.commit()
                   return render_template("thankyou.html")    
             
         
if __name__=='__main__':
     app.run(debug=True)