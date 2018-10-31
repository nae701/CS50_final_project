import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # Checks on the server if values were entered, if not shows error message
    if not request.form.get("name"):
        return render_template("error.html", message="Please fill in your name")
    elif not request.form.get("concentration"):
        return render_template("error.html", message="Please fill in your concentration")

    # Writes a new row to the csv file after each form submission
    with open('survey.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow([request.form.get("name"), request.form.get("concentration"), request.form.get("year")])
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # Reads csv file and passes it on in the form of a list to sheet
    with open('survey.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        students = list(reader)
    return render_template("sheet.html", students=students)
