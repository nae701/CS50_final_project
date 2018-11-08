import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Collects pertinent info on user's stock and cash balance
    stocks = db.execute("SELECT symbol, name, SUM(shares) FROM transactions WHERE user_id = :user_id GROUP BY symbol", user_id = session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id = session["user_id"])
    grandTotal = cash[0]["cash"]

    # Updates current value of stocks
    for stock in stocks:
        stock["price"] = lookup(stock["symbol"])["price"]
        stock["total"] = stock["price"] * stock["SUM(shares)"]
        grandTotal += stock["total"]
    return render_template("index.html", cash = cash, stocks = stocks, grandTotal = grandTotal)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # If user submits a form
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Ensures a valid input and that user has enough cash to complete purchase
        if not symbol or not lookup(symbol):
            return apology("Enter a valid symbol")
        elif not shares.isdigit() or int(shares) == 0 :
            return apology("Enter a positive integer")
        if db.execute("SELECT cash FROM users WHERE id = :id", id = session["user_id"])[0]["cash"] < lookup(symbol)["price"] * int(shares):
            return apology("You do not have enough cash to complete this transaction")

        # Updates transaction log to show user has bought stock
        db.execute("INSERT INTO transactions (user_id, symbol, name, shares, price) VALUES (:user_id, :symbol, :name, :shares, :price)",
        user_id = session['user_id'], symbol = symbol, name = lookup(symbol)["name"], shares = shares, price = lookup(symbol)["price"])

        # Updates user's current cash balance
        db.execute("UPDATE users SET cash = cash - :cost WHERE id = :id", cost = lookup(symbol)["price"] * int(shares), id = session["user_id"])
        return redirect('/')
    else:
        return render_template("buy.html")



@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username = request.args.get("username")
    if len(username) >= 1 and not db.execute("SELECT * FROM users WHERE username = :username", username = request.args.get("username")):
        return jsonify(True)
    else:
        return jsonify(False)

@app.route("/fund", methods=["GET", "POST"])
@login_required
def fund():
    """Adds funds for user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        fund = int(request.form.get("fund"))

        # Ensures that all fields are inputted correctly
        if  fund <= 0:
            return apology("Enter a positive amount")

        # Updates user's cash balance to include new funds
        db.execute("UPDATE users SET cash = cash + :fund WHERE id = :id", fund = fund, id = session["user_id"])

        return redirect('/')
    else:
        return render_template("fund.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stocks = db.execute("SELECT symbol, shares, price, time FROM transactions WHERE user_id = :user_id", user_id = session["user_id"])

    return render_template("history.html", stocks = stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get or not lookup(request.form.get("symbol")):
            return apology("Enter a valid symbol")
        quotes = lookup(request.form.get("symbol"))
        return render_template("quoted.html", quotes = quotes)
    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensures that all fields are inputted correctly
        if not request.form.get("username"):
            return apology("Enter username")
        elif not request.form.get("password") or not request.form.get("confirmation") :
            return apology("Enter or confirm password")
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("Passwords must match")

        hash = generate_password_hash(request.form.get("password"))

        # Saves user's info unless username is already in use
        result = db.execute("INSERT INTO users(username, hash) VALUES(:username, :hash)", username = request.form.get("username"), hash = hash)
        if not result:
            return apology("Username already exists")
        session["user_id"] = result
        return redirect('/')
    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # If user submits a form
    if request.method == "POST":
        shares = request.form.get("shares")
        symbol = request.form.get("symbol")

        # Ensures valid inputs
        if not symbol or not shares.isdigit:
            return apology("Enter a symbol and positive integer")
        shares = int(shares)

        # Ensures that a malicious user does not sell stock they do not own
        stock = db.execute("SELECT SUM(shares) FROM transactions WHERE user_id = :user_id AND symbol = :symbol", user_id = session["user_id"], symbol = symbol)
        if stock is None:
            return apology("You do not own that stock")
        if shares > stock[0]["SUM(shares)"]:
            return apology("You do not have enough shares of that stock to sell")

        # Logs sale but with a negative quantity
        db.execute("INSERT INTO transactions (user_id, symbol, name, shares, price) VALUES (:user_id, :symbol, :name, :shares, :price)",
        user_id = session['user_id'], symbol = symbol, name = lookup(symbol)["name"], shares = -shares, price = lookup(symbol)["price"])
        db.execute("UPDATE users SET cash = cash + :sale WHERE id = :id", sale = lookup(symbol)["price"] * shares, id = session["user_id"])
        return redirect("/")
    else:
        # Find what stocks one has to sell
        stocks = db.execute("SELECT symbol, SUM(shares) FROM transactions WHERE user_id = :user_id GROUP BY symbol", user_id = session["user_id"])
        return render_template("sell.html", stocks = stocks)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
