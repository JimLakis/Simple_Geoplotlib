# Simple use of Geoplotlib
# Python v 3.6
# 5/15/2018

import geoplotlib
from geoplotlib.utils import read_csv


data = read_csv('data/mtb_ride_data.csv')
geoplotlib.dot(data)
geoplotlib.show()
