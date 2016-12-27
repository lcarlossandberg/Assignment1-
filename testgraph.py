from graph import Greengraph
from nose.tools import assert_almost_equal, assert_equal
from mock import Mock, patch
import geopy
import numpy as np


def test_geolocate_int(): #test uses internet to check geolocate works
    latitude_longitude=Greengraph("","").geolocate('New York')
    assert_almost_equal(latitude_longitude[0], 40.7127, places=2)
    assert_almost_equal(latitude_longitude[1], -74.0059, places=2)

def test_geolocate(): #without internet
    with patch.object(geopy.geocoders.GoogleV3,'geocode') as mock_geocode:
         Greengraph('New York','Chicago').geolocate('New York')
         mock_geocode.assert_called_with('New York', exactly_one=False)


def test_location_sequence():#tried to use nose but doesnt work with tuples
    lls=Greengraph.location_sequence(Greengraph("",""), (0,0),(100,100),3)
    np.testing.assert_equal(lls[0],(0,0))
    np.testing.assert_equal(lls[1],(50,50))



test_geolocate_int()
test_geolocate()
test_location_sequence()



