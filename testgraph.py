from graph import Greengraph
from nose.tools import assert_almost_equal
from mock import Mock, patch
import geopy


def test_geolocate_int(): #test uses internet to check geolocate works
    latitude_longitude=Greengraph("","").geolocate('New York')
    assert_almost_equal(latitude_longitude[0], 40.7127, places=2)
    assert_almost_equal(latitude_longitude[1], -74.0059, places=2)

def test_geolocate(): #without internet
    with patch.object(geopy.geocoders.GoogleV3,'geocode') as mock_geocode:
         Greengraph('New York','Chicago').geolocate('New York')
         mock_geocode.assert_called_with('New York', exactly_one=False)

test_geolocate_int()
test_geolocate()






