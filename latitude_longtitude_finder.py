import tkinter as tk
import webbrowser

def open_location_in_maps():
    latitude = latitude_entry.get()
    longitude = longitude_entry.get()

    try:
        # Construct the Google Maps URL with the latitude and longitude
        url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

        # Open the URL in the default web browser
        webbrowser.open(url)
    except Exception as e:
        result_label.config(text="Error: Invalid latitude/longitude values")

# Create main window
root = tk.Tk()
root.title("Google Maps Locator")

# Latitude entry
latitude_label = tk.Label(root, text="Latitude:")
latitude_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
latitude_entry = tk.Entry(root)
latitude_entry.grid(row=0, column=1, padx=5, pady=5)

# Longitude entry
longitude_label = tk.Label(root, text="Longitude:")
longitude_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
longitude_entry = tk.Entry(root)
longitude_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to open location
locate_button = tk.Button(root, text="Locate", command=open_location_in_maps)
locate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
