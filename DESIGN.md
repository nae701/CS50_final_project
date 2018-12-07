Solving the Harvard Labyrinth

My program is a simple website that uses a Python web framework called Flask, to generate HTML pages. There is a small
amount of javascript, as well as some CSS for styling. I also use Google's Geolocation API to find the location of the user.

The first thing I needed to do to implement my project was to find the floor plans of the houses. Some of the floor
plan PDFs were in separate files so I used a free PDF merger online to combine them. However, some of the house floor
plans were unavaibale online and I had to make do with those I found. I stored these PDF files using CS50 IDE's file
system rather than using a database, because there were not that many files, and some of the files were rather large.
Using the CS50 IDE file system, it also made it easier to load the PDFs to the webpage since I used Jinja variables
that stored the requested house's name in the source attribute when using the embed tag in "place.html".

Now that I had found a way to have the user view PDFs of the floor plans I had stored in my file system, I wanted to
create several ways a user could access the floor plan information. All three methods are present on the main page of
the website. The first method was to use a search box.I used a search box rather than a dropdown menu for speed and
convenience of the user, since it may actually take more time to look through all the options to find the desired
house compared to quickly typing the name. I did error checking on the backend, using Python to determine if anything
was entered, and if something was entered, whether it existed in the system, otherwise it would return error. Rather
than checking if the user input is in my list of houses, I checked whether any element in my list was found in the
user input, so that the user could theoretically input "The Harvard Home of Lowell", or something equally bizzare,
and the application would still return the floor plans of Lowell.

The other method was simply clicking on the "Houses" link, which would show links to all the available house floor plans.
This was more difficiult than I had anticipated, since I had to use javascript to send a hidden form when the link was clicked,
so that the floor plans could be accessed VIA the POST method, otherwise the main page would have loaded.

The most difficult method to implement (but the easiest and simplest for the user to use), was clicking on the "Use geolocation"
button. I used Google's Geolocation API, where I would send a POST request to the API, and it would return a response. I then
converted this response into a JSON object, so that I could then access the coordinates of the result using keys. From here,
I had to implement an algorithm that found the distance between the user and central reference points in each house neigbhorhood
as determined by me on Google Maps. I then found the minimum distance, and returned a rendered HTML page that included links to
houses that were in the closest neighborhood.

A possible future extension that I was unable to implement, is to show a splitview where half the page is the floor plan, and the
other half is a Google Maps viewer that shows your current location, so as to facilitate navigation more than either could alone.