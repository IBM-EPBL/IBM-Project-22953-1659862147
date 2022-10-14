from flask import Flask,render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html', name="Home")

@app.route("/about")
def about():
  return render_template('about.html', name="About")


@app.route("/signin")
def login():
  return render_template('sign_in.html', name="signin")

@app.route("/signup")
def signup():
  return render_template('sign_up.html', name="signup")

@app.route('/addlist',methods = ['POST', 'GET'])
def addlist():
   if request.method == 'POST':
      try:
         name = request.form['name']
         email = request.form['email']
         addr = request.form['address']
         password = request.form['password']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,email,addr,password) VALUES (?,?,?,?)",(name,email,addr,password) )
            con.commit()
            msg = "Successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("list.html",name="list")
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from candidates")
   
   candidates = cur.fetchall();
   return render_template("list.html", candidates = candidates)

if __name__ == '__main__':
   app.run(debug = True)