import os, sys
import webbrowser
import time


global gps_Location_kml_files
gps_Location_kml_files = "gps_REPORT_kml"


def kml_file_generate(kml_lattitude,kml_longitude):
    
    global gps_Location_kml_files
    with open(gps_Location_kml_files+"/position.kml","w")as pos:
        pos.write("""<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Placemark>
            <name> Live_GPS </name>
            <Point>
                    <coordinates>%s,%s,0</coordinates>
            </Point>
    </Placemark>
    </kml>""" % (kml_lattitude,kml_longitude))
    open_map()
   
def open_google_Earth():
    
    import subprocess
    subprocess.Popen([r"C:\Program Files\Google\Google Earth Pro\client\googleearth.exe"])
    
def open_map():
    
    import webbrowser
    gps_Location_kml_files
    url="C:/Users/USER/Desktop/Googleearth/gps_REPORT_kml/position.kml"
    webbrowser.open(url, new=2)

open_google_Earth()

while(1):
    longitude = input("Enter your longitude: ")
    lattitude = input("Enter your lattitude: ")
    kml_file_generate(lattitude,longitude)
 























































































