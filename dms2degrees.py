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
# dms2degrees.py converts degrees-minutes-seconds to decimal degrees 
# 
# usage: dms2degrees.py -f /path/to/dms.txt
#		An example of dms.txt
# 		20 0 44.44
#		-75 59 15.555
#		...
# note: most online converters round the numbers, this function does not! so it is much more precise. 
# see also: degrees2dms.py
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
    	dms = [float(col.strip()) for col in line.split()]
    	degrees = dms[0] + np.divide(dms[1],60) + np.divide(dms[2],3600)
    	print(Decimal(degrees))