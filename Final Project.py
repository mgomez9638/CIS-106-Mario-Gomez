# Final Project
# This program reads data from a url using Internet processing methods and builds arrays for each indentation using XML functions.
# Afterwards, it displays the catalog items information, the amount of items, and the average price of the items.
#
# References:
#     https://docs.python.org/3/py-modindex.html
#     https://docs.python.org/3/library/urllib.html#module-urllib
#     https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
#     https://realpython.com/python-itertools/
#     https://realpython.com/python-zip-function/


import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree


def find_xml():
    try:
        url = "https://www.w3schools.com/xml/cd_catalog.xml"
        xml_file = urllib.request.urlopen(url)
        return xml_file
    except urllib.error.HTTPError:
        print("URL is incorrect!")
        print(sys.exc_info()[1])
    except urllib.error.URLError:
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


def get_total(xml_file, price):
    try:
        total = sum(price)
        return total
    except ValueError:
        print("Missing data", xml_file)
        print(sys.exc_info()[1])
    except TypeError:
        print("Wrong type", xml_file)
        print(sys.exc_info()[1])


def get_avg_price(xml_file, total, price):
    try:
        avg_price = round(total/len(price), 2)
        return avg_price
    except ZeroDivisionError:
        print("Missing values", xml_file)
        print(sys.exc_info()[1])
    except ValueError:
        print("Missing data", xml_file)
        print(sys.exc_info()[1])
    except TypeError:
        print("Wrong type", xml_file)
        print(sys.exc_info()[1])


def display_result(xml_file, title, artist, country, price, year, avg_price):
    try:
        print("Catalog items information for CDs in the system:\n\n")
        print("Title - Artist - Country - Price - Year\n")
        for titles, artists, countries, prices, years in zip(title, artist, country, price, year):
            print(titles, "-", artists, "-", countries, "-", prices, "-", years, "\n")
        print("\nThe amount of catalog items and the average price of each one:\n")
        print(len(title), "item(s) - $", avg_price, "average price")
    except AttributeError:
        print("Wrong Type", xml_file)
        print(sys.exc_info()[1])
    except IndexError:
        print("Incorrectly formatted", xml_file)
        print(sys.exc_info()[1])
    except ValueError:
        print("Missing data", xml_file)
        print(sys.exc_info()[1])


def main():
    print("\t\tWelcome to Programming with XML Files using Element Tree!\n\n")
    xml_file = find_xml()
    title, artist, country, price, year = get_xml_info(xml_file)
    total = get_total(xml_file, price)
    avg_price = get_avg_price(xml_file, total, price)
    display_result(xml_file, title, artist, country, price, year, avg_price)
    print("\n\n\t\tThank You for Programming with XML Files using Element Tree!\n\n")


main()
