# SpatialTinkering - Tinkering with spatial data.
# Copyright (C) 2017  Amin Sarafraz
#
# This program is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
# degrees2dms.py converts decimal degrees to degrees-minutes-seconds
# 
# usage: degrees2dms.py -f /path/to/degrees.txt
#		An example of degrees.txt
# 		20.012345678901230
# 		20.012345678901231
# 		20.012345678901232
#		-75.987654321012345
#		-75.987654321012346
#		-75.987654321012347
#		...
# note: most online converters round the numbers, this function does not! so it is much more precise. 
# see also: dms2degrees.py

from __future__ import print_function
from decimal import Decimal
import argparse
import numpy as np

# construct the argumnent parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f","--file", help = "File path")
args = vars(ap.parse_args())
fname = args["file"]

# read the file line by line and put each row in a list
with open(fname) as f:
    for line in f:
    	latlongs = [float(col.strip()) for col in line.split()]
    	degrees = np.fix(latlongs)
    	minutes = np.fix(np.mod(np.multiply(np.absolute(latlongs),60),60))
    	seconds = np.mod(np.multiply(np.absolute(latlongs),3600),60)
    	print(Decimal(degrees[0]), Decimal(minutes[0]), Decimal(seconds[0]))