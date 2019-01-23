from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for, make_response
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import datetime
import requests
import json
import random
from random import shuffle

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response



# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")


@app.route("/")

def index():

    return render_template("index.html")


@app.route("/spelregels")
def spelregels():

    return render_template("spelregels.html")

@app.route("/scoreOnline")
def scoreOnline():
    scoreOnline = db.execute("SELECT username, score FROM scores ORDER BY score DESC")
    return render_template("scoreOnline.html", scoreOnline=scoreOnline)

@app.route("/speelpagina")
def speelpagina():

    return render_template("speelpagina.html")


@app.route("/account")
def account():
    lijst = db.execute("SELECT username, score FROM scores WHERE id = :id ORDER BY score DESC", id = session["user_id"])
    scores = []
    for symbolDict in lijst:
        gebruikersnaam = symbolDict["username"]
        rowDict = {}
        rowDict["score"]=symbolDict["score"]
        scores.append(rowDict)

    return render_template("account.html", gebruikersnaam = gebruikersnaam, scores = scores)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows=db.execute("SELECT * FROM users WHERE username = :username", username = request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        #remember username
        session["username"] = rows[0]["username"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():

    """Register user."""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username")

        elif not request.form.get("password"):
            return apology("must provide password")

        elif not request.form.get("confirmation"):
            return apology("must provide password (again)")

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords not the same")

        password = pwd_context.hash(request.form.get("password"))

        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hashpassword)",
                                username=request.form.get("username"),
                            hashpassword=password)

        if not result:
            return apology("The username is already taken")

        rows=db.execute("SELECT * FROM users WHERE username = :username",
                                   username=request.form.get("username"))

        session["user_id"] = rows[0]["id"]

        #remember username
        session["username"] = rows[0]["username"]

        return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/speelopties")
def speelopties():

    return render_template("speelopties.html")


@app.route("/eindresultaat", methods=['GET'])
def eindresultaat():

    Answers = {}
    return render_template("eindresultaat.html", Answers = Answers)

@app.route('/api', methods=['GET','POST'])
def api():
    if request.method == "POST":
        Answers = request.get_json()

        username = session["username"]

        good = []
        for i in range(10):
            try:
                if Answers["ca" + str(i)] == Answers["a" + str(i)]:
                    good.append("True")
                else:
                    good.append("False")
            except KeyError:
                good.append("False")

        Score = 0
        for i in good:
            if i == "True":
                Score += 1
            else:
                Score == Score

        db.execute("INSERT INTO 'scores' (id, username, score) VALUES(:id, :username, :Score)",
                   id =session["user_id"], username = username, Score=Score)

        return render_template("eindresultaat.html", Answers = Answers, Score = Score)

    else:
        iCategory = request.args.get('category')
        iAmount = request.args.get('amount')

        if iCategory != "-1":
            url = "https://opentdb.com/api.php?amount="+iAmount+"&category="+iCategory+"&medium=medium"+"&type=multiple"
            # get the data corresponded to the url
            data = requests.get(url).text
            data = data.replace("&quot;","'")
            data = data.replace("&#039;", "'")
            data = data.replace("&amp;", "&")
            data = data.replace("I&ntilde;&aacute;rritu;", " ")
            data = data.replace("Zeln&iacute;čkov&aacute;","Zelníčková")
            data = data.replace("&acute;","a")
            data = data.replace("&ecute;","e")

            data = json.loads(data)
            # format first question:
            questions = []
            for entry in data["results"]:
                q = [x for x in entry["incorrect_answers"]]
                q.append(entry["correct_answer"])
                q = sorted(q, key = lambda x: random.random() )

                entry["random_answers"] = q
                questions.append(entry)

        else:
            questionHolder = []
            for num in ['11','12','15','21','26']:
                url = "https://opentdb.com/api.php?amount="+'2'+"&category="+num+"&medium=medium"+"&type=multiple"
                data = requests.get(url).text
                data = data.replace("&quot;","'")
                data = data.replace("&#039;", "'")
                data = data.replace("&amp;", "&")
                data = data.replace("I&ntilde;&aacute;rritu;", " ")
                data = data.replace("Zeln&iacute;čkov&aacute;","Zelníčková")
                data = data.replace("&acute;","a")
                data = data.replace("&ecute;","e")
                data = json.loads(data)
                # format first question:
                questionHolder.append(data["results"][0])
                questionHolder.append(data["results"][1])

            # format first question:
            questions = []
            for entry in questionHolder:
                q = [x for x in entry["incorrect_answers"]]
                q.append(entry["correct_answer"])
                q = sorted(q, key = lambda x: random.random() )

                entry["random_answers"] = q
                questions.append(entry)

            questions = sorted(questions, key = lambda x: random.random() )

        return render_template('api.html', url=url, output=data, questions = questions)

"https://opentdb.com/api.php?amount=10&category=20&difficulty=medium&type=multiple"






