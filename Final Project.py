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
 

def get_xml_info(xml_file):
    title = []
    artist = []
    country = []
    price = []
    year = []
    music = xml.etree.ElementTree.parse(xml_file)
    subject = music.getroot()
    try:
        for cd in subject.findall("CD"):
            titles = cd.find("TITLE").text
            title.append(titles)
            artists = cd.find("ARTIST").text
            artist.append(artists)
            countries = cd.find("COUNTRY").text
            country.append(countries)
            prices = cd.find("PRICE").text
            price.append(float(prices))
            years = cd.find("YEAR").text
            year.append(years)
        return title, artist, country, price, year
    except NameError:
        print("Incorrect Name", xml_file)
        print(sys.exc_info()[1])
    except AttributeError:
        print("Wrong Type", xml_file)
        print(sys.exc_info()[1])
    except IndexError:
        print("Incorrectly formatted", xml_file)
        print(sys.exc_info()[1])
    except ValueError:
        print("Missing data", xml_file)
        print(sys.exc_info()[1])
 
