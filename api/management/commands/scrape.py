#
# Waze Place Discover & Audit (WPDA)
# Version 1.1, 2016-12-07
# Copyright 2016 David Nelson. All rights reserved.
#

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

		# Create a 2D list to store the parsed database
		place = []
		place.append([])
		row = -1		# Start at -1 because it will auto-increment to 0 with the first iteration
		col = 0
		index = 0

		# Parse through the data as follows:
		# 1. Find each instance of <td> and note the index in the string
		# 2. Starting at that position, look for the first instance of </td>
		# 3. Store the string value between the two found index positions
		# 4. Every 15 found fields, begin a new row denoting a new Place entry
		while index < len(data):
			try:
				start = data.find("<td>", index)
				if col == 15:			# A new venue entry begins every 15 fields
					place.append([])
					row+= 1
					col = 0
				end = data.index("</td>", start)
				place[row].append(data[start+4:end])
				index = end
			except ValueError:
				return ""

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
		self.scrape(regex)
