#
# Waze Place Discover & Audit (WPDA)
# Version 0.9.9, 2016-10-30
# Copyright 2016 David Nelson. All rights reserved.
#

from bs4 import BeautifulSoup
import sys, requests, re, os

def scrape():
	# Inital setup
	venue = "hy[ -]?vee"
	use_regex = 1
	ignore_case = 1
	max_lock = 6
	country = 235

	payload = {"vname": venue, "regex": use_regex, "ignorecase": ignore_case, "lock": max_lock, "country": country, "submit": "Search"}
	#scrape = requests.post("https://db.slickbox.net/venues.php", data = payload)

	# ------------------------------------- Parse the HTML Output -------------------------------------- #

	scrape = open("/home/dnelson/Desktop/Hy-Vee.html").read()
	# Find where the relevant data begins and ends in the HTML output
	data = scrape[scrape.find('<tr id="link"'):scrape.rfind('</table>')]
	#data = scrape.text[scrape.text.find('<tr id="link"'):scrape.text.rfind('</table>')]

	# Fill empty fields with text to prevent BS from erasing them, then initialize BS
	data = data.replace("<td></td>", "<td>(NULL)</td>")
	soup = BeautifulSoup(data, "html.parser")

	# Extract the permalinks and add them as the next element after the venue name
	for i in soup.find_all("a"):
		i.insert(1, i.get("href"))

	# Keep only the readable text and use a CSV-friendly delimiter
	soup = soup.get_text('","')

	# Clean up the output
	soup = soup.replace('"," ', '","')	# Remove extra spaces
	soup = soup.replace("(NULL)", "")	# Remove the random text

	# Split on the field delimiter
	split = re.split('","', soup)

	# Generate a 2D list of from the fields
	venues = []
	count = -1		# Start at -1 because it will auto-increment to 0 with the first iteration
	for i in range(len(split)):
		if i % 13 == 0:			# A new venue entry begins every 13 fields
			venues.append([])
			count+= 1
		venues[count].append(split[i])

	# ------------------------------------- Export to the Database ------------------------------------- #

	for row in venues:
		ven_id = re.findall("(?!.*[venues=]).*", row[1])
		#values = '","'.join(row)
		#values = '"'+ str(venue_id[0]) +'","'+ values +'"'	# Prepend the Venue ID and add quotes
		
		new = Place(is_verified=False, venue_id=ven_id[0], name=row[0], permalink=row[1], lock_level=row[2], categories=row[3], number=row[4], street=row[5], city=row[6], state=row[7], country=row[8], updated_by=row[9], updated_on=row[10], user_report_on=row[11], is_residential=row[12])
		new.save()

# File starts here
if __name__ == '__main__':
	import django
	from django.conf import settings
	
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wpda.settings")
	django.setup()

	from api.models import Place
	scrape()
