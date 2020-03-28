# Final Project
# This program reads data from a url using Internet processing methods and builds arrays for each indentation using XML functions.
# Afterwards, it displays the catalog items, the amount of items, and the average price of the items.
#
# References:
#     https://docs.python.org/3/py-modindex.html


import sys
import urllib.request
import urllib.error


def find_xml():
    try:
        url = "https://www.w3schools.com/xml/cd_catalog.xml"
        xml_file = urllib.request.urlopen(url)
        return xml_file
    except urllib.error.HTTPError:
        print("URL is incorrect!")
        print(sys.exc_info()[1])
    except urrlib.error.URLError:
        print("URL information is incorrect!")
        print(sys.exc_info()[1])
 
