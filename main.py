import flask
from flask import Flask, render_template, redirect, request
import sqlite3

from werkzeug.utils import redirect

conn = sqlite3.connect("Movie_Bookings.db", check_same_thread=False)
cursor = conn.cursor()

Movies_table = conn.execute("SELECT name from sqlite_master WHERE type='table' AND name='MOVIES'").fetchall()


if Movies_table:
    print("Table Already Exists ! ")
else:
    conn.execute(''' CREATE TABLE MOVIES(
                            movie_iD INTEGER PRIMARY KEY AUTOINCREMENT,
                            movie_name TEXT
                            length INTEGER,
                            language TEXT,
                            show_start TEXT
                             show_end TEXT,
                             city_name TEXT); ''')
    print("Table has created...!")



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("Home.html")


@app.route("/login-admin", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        getUname = request.form["uname"]
        getpass = request.form["pswd"]
    try:
        if getUname == 'admin' and getpass == "12345":
            return redirect("/dashboard")
        else:
            print("Invalid username and password")
    except Exception as e:
        print(e)

    return render_template("/admin_login.html")


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        getmovie_name = request.form['movie_name']
        getlength = request.form['length']
        getlanguage = request.form['language']
        getshow_start = request.form['show_start']
        getshow_end = request.form['show_end']
        getcityname = request.form['city_name']


        print(getmovie_name)
        print(getlength)
        print(getlanguage)
        print(getshow_start)
        print(getshow_end)
        print(getcityname)


    try:
        data=(getmovie_name,getlength,getlanguage,getshow_start,getshow_end,getcityname)
        query = "INSERT INTO MOVIES(movie_name,length,language,show_start,show_end,city_name)VALUES(?,?,?,?,?,?)"
        cursor.execute(query,data)
        print(query)
        conn.commit()
        return redirect("/viewall")
    except Exception as e:
        print(e)

    return render_template("/dashboard.html")

@app.route("/viewall")
def viewall():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MOVIES")
    result = cursor.fetchall()
    return render_template("viewall.html", student=result)




if (__name__) == "__main__":
    app.run(debug=True)