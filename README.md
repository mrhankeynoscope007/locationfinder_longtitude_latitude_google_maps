# locationfinder_longtitude_latitude_google_maps
locationfinder_longtitude_latitude_google_maps


This script creates a simple GUI application using Tkinter for locating a specific latitude and longitude on Google Maps.

Here's a breakdown of how it works:

The open_location_in_maps() function is called when the user clicks the "Locate" button. It retrieves the latitude and longitude values entered by the user from the respective entry fields.
It constructs a Google Maps URL with the latitude and longitude values as parameters.
The URL is then opened in the default web browser using the webbrowser.open() function.
If an error occurs during the process, such as invalid latitude or longitude values, an error message is displayed in the result label.
The GUI consists of:

Two entry fields for the user to input latitude and longitude values.
A "Locate" button to trigger the location lookup.
A result label to display any error messages.
When you run the script, it will open a window where you can enter latitude and longitude values. Clicking the "Locate" button will open Google Maps in your default web browser, displaying the location corresponding to the provided latitude and longitude values. If there are any errors, such as invalid input, they will be displayed in the result label.

Python3.11.5
