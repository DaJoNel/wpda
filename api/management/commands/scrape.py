#
# Waze Place Discover & Audit (WPDA)
# Version 1.1, 2016-12-07
# Copyright 2016 David Nelson. All rights reserved.
#

from bs4 import BeautifulSoup
import sys, requests, re, os, iso8601

from django.core.management.base import BaseCommand, CommandError
from api.models import Place

class Command(BaseCommand):
	args = "\"[regex]\" (quotes matter)"
	help = "WPDA place data scraper."

	def scrape(self):
		# Setup search query
		print(sys.argv[2])
		venue = sys.argv[2]
		use_regex = 1
		ignore_case = 1
		max_lock = 6
		country = 235

		payload = {"vname": venue, "regex": use_regex, "ignorecase": ignore_case, "lock": max_lock, "country": country, "submit": "Search"}
		scrape = requests.post("https://db.slickbox.net/venues.php", data = payload)

		# ------------------------------------- Parse the HTML Output -------------------------------------- #

		# Find where the relevant data begins and ends in the HTML output
		data = scrape.text[scrape.text.find('<tr id="link"'):scrape.text.rfind('</table>')]

		# Fill empty fields with text to prevent BS from erasing them, then initialize BS
		data = data.replace("<td></td>", "<td>(NULL)</td>")
		soup = BeautifulSoup(data, "html.parser")

		# Extract the permalinks and add them as the next element after the venue name
		for i in soup.find_all("a"):
			i.insert(1, i.get("href"))

		# Keep only the readable text and arbitrarily use an uncommon delimiter
		soup = soup.get_text('__')

		# Clean up the output
		soup = soup.replace('__ ', '__')	# Remove extra spaces
		soup = soup.replace("(NULL)", "")	# Remove the random text added earlier

		# Split on the field delimiter
		split = re.split('__', soup)

		# Generate a 2D list of from the fields
		place = []
		count = -1		# Start at -1 because it will auto-increment to 0 with the first iteration
		for i in range(len(split)):
			if i % 15 == 0:			# A new venue entry begins every 15 fields
				place.append([])
				count+= 1
			place[count].append(split[i])

		# ------------------------------------- Export to the Database ------------------------------------- #

		for row in place:
			ven_id = re.findall("(?!.*[venues=]).*", row[1])	# Extract the venue ID

			# Generate a Python datetime object for each date field
			if row[10] != "":
				row[10] = iso8601.parse_date(row[10])
			else:
				row[10] = None		# If there is no time listed, do not attempt to parse

			if row[12] != "":
				row[12] = iso8601.parse_date(row[12])
			else:
				row[12] = None

			# We care whether there has been a place update request, not the date
			if row[13] != "":
				row[13] = True
			else:
				row[13] = False

			# Add the row to the database
			new = Place(venueId=ven_id[0], name=row[0], permalink=row[1], lockLevel=row[2],
			categories=row[3], number=row[4], street=row[5], city=row[6], state=row[7],
			country=row[8], createdBy=row[9], createdOn=row[10], updatedBy=row[11],
			updatedOn=row[12], updateRequest=row[13], isResidential=row[14])
			new.save()

	def add_arguments(self, parser):
		parser.add_argument('regex')

	def handle(self, *args, **options):
		regex = options['regex']
		self.scrape()
