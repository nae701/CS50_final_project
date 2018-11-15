# View As

## Questions

9.1. An access token is opaque string (a string that is handled by the compiler but actually
interpreted like other values), that allows the app using the access token to determine a specifc
user, app, or page. Included information in the access token is when it will expire and which
app generated the token.


9.2. There were 3 bugs that when combined together posed a security threat. The first bug was that the View As
feature was meant to be a view only interface, however it incorrectly allowed one to post a video, in the
composer that lets you wish your friends happy birthday. The second bug was the video uploader incorrectly
generated an access token which had the permissions of the mobile facebook app. The third bug is that when
the video uploader was accessed during View As, it would incorrectly generate an access token of the user being
viewed instead for the user that is doing the viewing. That access token was then accessible in the html for the page.

9.3. The access token only allows temporary access to approved and logged in applications. If a user is logged out
it would clear any current access tokens and would require the user to login into the relevant apps again. Thus by forcibly
logging out users, Facebook made sure that any potentially stolen access tokens would be useless.

9.4. Session cookies expire when the browser is closed or when the user logs out, whereas access tokens are either short lived or long lived.
Short lived tokens may last a couple of hours whereas long lived tokens can last around 60 days as long as the user
doesn't log out, regardless of if the browser is closed or not since the token is stored on the device instead of the browser like a cookie.


## Debrief

a. Facebook documentation

b. 60 minutes
