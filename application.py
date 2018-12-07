import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
import requests
import math
import json


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


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

HOUSES = ["adams", "dunster", "eliot", "kirkland", "lowell", "mather", "quincy", "winthrop"]


@app.route("/", methods=["GET", "POST"])
def index():

    # If user arrives at page by submitting a form
    if request.method == "POST":
        place = request.form.get("place")

        # Checks if user entered a place
        if not place:
            return render_template("error.html", message="Enter a valid place")

        # Checks if entered place is in system and returns floor plans, else prints error
        for house in HOUSES:
            if house in place.lower():
                return render_template("place.html", place=house)

        return render_template("error.html", message="Sorry, " + place + " is not currently in our system")

    # If user arrives at page through URL
    else:
        return render_template("index.html")


@app.route("/houses")
def houses():

    # Renders a page with all available houses
    return render_template("houses.html", title="House", HOUSES=HOUSES, n=range(len(HOUSES)))


@app.route("/geo", methods=["GET", "POST"])
def geo():
    """Reccommends the closest group of houses based on user's geolocation"""

    # If user arrives at page by submitting a form
    if request.method == "POST":

        # GPS coordinates of approximate center of each house neighborhood
        river_west = [42.371501, -71.117476]
        river_west_houses = ["kirkland", "eliot", "winthrop"]

        river_central = [42.370613, -71.120223]
        river_central_houses = ["adams", "quincy", "lowell"]

        river_east = [42.368948, -71.115889]
        river_east_houses = ["mather", "dunster"]

        # Accessing Google Geolocation API and extracting user's current GPS coordinates
        response = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAftpeFjJjTV6fH6r4FAZ2EUXpvpo5Dgm0")
        position = response.json()
        location = [float(position["location"]["lat"]), float(position["location"]["lng"])]

        # Finds the closest house neighborhood based on user's GPS coordinates
        dist_river_west = math.sqrt(((river_west[0] - location[0])**2) + ((river_west[1] - location[1])**2))
        dist_river_central = math.sqrt(((river_central[0] - location[0])**2) + ((river_central[1] - location[1])**2))
        dist_river_east = math.sqrt(((river_east[0] - location[0])**2) + ((river_east[1] - location[1])**2))
        dist_min = min(dist_river_east, dist_river_central, dist_river_west)

        # Reccommends the closest house neighborhood by loading links to those floor plans
        if dist_min == dist_river_east:
            return render_template("houses.html", title="River East", HOUSES=river_east_houses, n=range(len(river_east_houses)))
        elif dist_min == dist_river_central:
            return render_template("houses.html", title="River Central",  HOUSES=river_central_houses, n=range(len(river_central_houses)))
        elif dist_min == dist_river_west:
            return render_template("houses.html", title="River West", HOUSES=river_west_houses, n=range(len(river_west_houses)))
    else:
        return render_template("geo.html")

