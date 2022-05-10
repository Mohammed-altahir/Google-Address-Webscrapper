This is a simple webscrapper that garthers a detailed address for a given location 
example : "Empire State Building" and it's address "20 W 34th St, New York, NY 10001, United States"

This location is scraped from a pdf file and output the result in "results.json" within it the result is like this:

[
    {
        "name": "John Doe",
        "address": "Empire State Building",
        "google_maps_address": "20 W 34th St, New York, NY 10001, United States"
    }, 
    
    {
        "name": "Jane Doe",
        "address": "Flatiron Building",
        "google_maps_address": "175 5th Ave, New York, NY 10010, United States"
    }
]

Then its stored in a SQLite3 database 
(of course you can choose whatever database that suite you i picked this up because it fast and don't need any server setup )

remember to when you change the output file "result.json" change it in every python file 
and the default database name is "database" and for the table "YOUR TABLE NAME"

ALSO DON'T FORGET THE WEBDIRVER , PUT IN THE ROOT DIRECTORY OF THIS PROJECT
I tried chrome and Microsoft Egde webdrivers and they are working fine 

REMEBER TO CHECK THE VERSION OF YOUR BROWESER BEFORE DOWNLOADING THE WEBDRIVER
