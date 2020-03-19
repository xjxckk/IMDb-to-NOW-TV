# Your IMDb watchlist filtered for NOW TV availability.
This script checks all movies and TV shows on your IMDb watchlist and checks if they are available on Now TV.
If they are they will be added to a seperate list.

## Installation
You will need Python, Selenium & Beautiful Soup installed.

## Quickstart
Download the respository as a zip file and extract it to a folder.

Go to your IMDb watchlist and scroll to the bottom, click on export this list and put the WATCHLIST.csv file in the same folder as the script.

Open the config.txt file and replace "email" with your IMDb email and "password" with your IMDb password.

Run the IMDb to NOW TV.py script.

Access your new list by clicking your username for the dropdown on IMDb and clicking "Your lists".

Enjoy!

## Misc
Uses [nowtv.maft.uk](ad) to check for NOW TV availability.

To check for false positives refine your new list by Not in watchlist (under You and This List).
