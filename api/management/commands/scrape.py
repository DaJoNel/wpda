#
# Waze Place Discover & Audit (WPDA)
# Version 1.2, 2016-12-09
# Copyright 2016 David Nelson. All rights reserved.
#

from bs4 import BeautifulSoup
import sys, requests, re, os, iso8601

from django.core.management.base import BaseCommand, CommandError
from api.models import Place

class Command(BaseCommand):
	help = "WPDA place data scraper."

	def scrape(self, regex):
		# Setup search query
		venue = regex
		use_regex = 1
		ignore_case = 1
		max_lock = 6
		country = 235

		payload = {"vname": venue, "regex": use_regex, "ignorecase": ignore_case,
		"lock": max_lock, "country": country, "submit": "Search"}
		scrape = requests.post("https://db.slickbox.net/venues.php", data = payload)

		# ------------------------------------- Parse the HTML Output -------------------------------------- #

		# Find where the relevant data begins and ends in the HTML output
		data = scrape.text[scrape.text.find('</thead>'):scrape.text.rfind('</table>')]

		# Fill empty fields with text to prevent BS from erasing them, then initialize BS
		soup = BeautifulSoup(data, "html.parser")

		# Split the permalinks into separate fields in order to make the data useful
		for a in soup.find_all("a"):
			# Create three new elements (soon to be database fields)
			permalink = soup.new_tag("td")
			permalink.string = a.get("href")

			name = soup.new_tag("td")
			name.string = a.string

			ven_id = soup.new_tag("td")
			ven_id.string = re.findall("(?!.*[venues=]).*", permalink.string)[0]

			# Add the new elements to the document tree
			a.parent.append(ven_id)
			a.parent.append(permalink)
			a.parent.append(name)

			# Clean up the original permalink
			a.decompose()
			ven_id.parent.unwrap()

		# Generate a 2D list of the fields
		place = []
		count = 0
		row = -1
		for child in soup.find_all("td"):
			if count % 16 == 0:			# A new venue entry begins every 16 fields
				place.append([])
				row+= 1
				count = 0
			if child.string is not None:
				place[row].append(child.string.strip())
			else:
				place[row].append(child.string)		# Cannot strip a NoneType
			count+= 1

		# ------------------------------------- Export to the Database ------------------------------------- #

		for row in place:
			# Generate a Python datetime object for each date field
			if row[11] != None:
				row[11] = iso8601.parse_date(row[11])

			if row[13] != None:
				row[13] = iso8601.parse_date(row[13])

			# We care whether there has been a place update request, not the date
			if row[14] != None:
				row[14] = True
			else:
				row[14] = False

			# Add the row to the database
			new = Place(venueId=row[0], permalink=row[1], name=row[2], lockLevel=row[3],
			categories=row[4], number=row[5], street=row[6], city=row[7], state=row[8],
			country=row[9], createdBy=row[10], createdOn=row[11], updatedBy=row[12],
			updatedOn=row[13], updateRequest=row[14], isResidential=row[15])
			new.save()

	def add_arguments(self, parser):
		parser.add_argument('regex')

	def handle(self, *args, **options):
		regex = options['regex']
		self.scrape(regex)
