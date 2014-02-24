import urllib2
from bs4 import BeautifulSoup

# Find and open the URL to scrape
url = 'http://ire.org/conferences/nicar-2014/schedule/'
html = urllib2.urlopen(url).read()

# Open an output file to put our scraper results
outfile = open('handsonpanel_2014.txt', 'a')

# Use BeautifulSoup to extract the course/panel list 
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

        # If that schedule item is a hands-on class ...
        if li.find('div', "col-10 heading5").text == 'Hands-on' or 'Panel':

            # Write the text title of that item to the output file.
            outfile.write(li.find('h3').text.encode('utf-8') + hr)