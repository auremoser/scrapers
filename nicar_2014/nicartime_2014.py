import urllib2
from bs4 import BeautifulSoup

# Find and open the URL to scrape
url = 'http://ire.org/conferences/nicar-2014/schedule/'
html = urllib2.urlopen(url).read()

# Open an output file to put our scraper results
outfile = open('nicartime_2014.txt', 'a')

# Use BeautifulSoup to extract the course list
# from the schedule page.
# Start by putting each of the daily schedule
# tabs on the page into a list, so we can loop
# over them one at a time.

soup = BeautifulSoup(html)
pane_uls = soup.findAll("ul", "listview pane")

hr = '\n' + ('-'*30) + '\n'
# Loop through each of the panes ...
for pane in pane_uls:

    # And then loop through each schedule item in each pane.
    for li in pane.findAll('li'):
        if li.find('div', "col-10 heading5").text:
            print li.text + hr
            outfile.write(li.find('div', "col-15 meta").text + hr)