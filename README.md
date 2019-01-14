# Solving the Harvard Labyrinth
# help users convienently find the floor plans of the Harvard Houses
The main purpose of my project is to help users convienently find the floor plans of the Harvard Houses. The idea came
from my struggles as a freshman (and even as a sophomore!) in trying to find a restroom or a specific room in a house that
I was unfamiliar with.

My project is a simple website application that is built using the Flask framework. In order to get the website server
up and running in CS50 IDE simply write "flask run" in the command line, ensuring that the current directory you are in
is "implementation/". Then click on the URL that is outputted in the terminal to open the main page of the website.

There are several different ways to access the floor plans. The user can search up their desired house (case insensitive),
by typing in the name of the house and clicking on the "search" button. Then the website will then load the floor plan PDFs
using an embedded PDF viewer. If the user attempts to search nothing, or inputs a string that is not found in the system, the
application will load an apologetic error page describing the error.

If the user does not rememeber exactly how to spell the name of the House, they can click on the "Houses" link in the upper
right of the navigation bar. This will load a page that returns links to all houses with available floor plans. Clicking
on any of these links will load that specific house's floor plans.

There is a third option for those who do not want to enter a search request or browse through all the houses. The user
can simply click on the "Use geolocation" button, and the website will load a page of the nearest house neighborhood (e.g. River
West). On this page, the user can then click on any of the individual house links to view those specific floor plans.

