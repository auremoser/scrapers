import urllib2
from bs4 import BeautifulSoup

# Find and open the URL to scrape
url = 'http://ire.org/conferences/nicar-2014/schedule/'
html = urllib2.urlopen(url).read()

# Open an output file to put our scraper results
outfile = open('nicar_2014.csv', 'a')

# Use BeautifulSoup to extract the course/panel list
# from the schedule page.
# Start by putting each of the daily schedule
# tabs on the page into a list, so we can loop
# over them one at a time.

soup = BeautifulSoup(html)
pane_uls = soup.findAll("ul", "listview pane")

hr = '\n' + ('-' * 30) + '\n'
outfile.write('Title|Location|Time\n')
# Loop through each of the panes ...
for pane in pane_uls:

    # And then loop through each schedule item in each pane.
    for li in pane.findAll('li'):

        # If that schedule item is a hands-on class ...
        if li.find('div', "col-10 heading5").text == 'Hands-on' or 'Panel':
            title = li.find('h3').text.encode('utf-8').strip()
            place, time = li.find('div', 'col-15 meta').find_all('p')
            output = title + '|' + place.get_text().encode('utf-8') + '|' + time.get_text().encode('utf-8') + '\n'
            print output
            outfile.write(output)
