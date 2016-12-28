from ..graph import Greengraph
from nose.tools import assert_almost_equal, assert_equal
from mock import Mock, patch
import geopy
import numpy as np
from itertools import cycle
import os

def test_init():
    with patch.object(geopy.geocoders, 'GoogleV3') as mock_GoogleV3:
        test_Greengraph = Greengraph('New York', 'Chicago')
        mock_GoogleV3.assert_called_with(domain="maps.google.co.uk")
        assert_equal(test_Greengraph.start, 'New York')
        assert_equal(test_Greengraph.end, 'Chicago')


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


def test_green_between_int():#test uses internet
    mygraph=Greengraph('New York','Chicago')
    data = mygraph.green_between(20)
    np.testing.assert_equal(data,(60300, 155604, 156609, 152544, 157774, 155776, 158681, 158232, 159028, 155403, 156967, 103487, 93931, 138503, 151500, 148021, 150200, 147648, 42961, 28124))


def test_green_between():
    mock_map = open(os.path.join(os.path.dirname(__file__),'fixtures','London.png'),'rb')
    mock_geolocate = Mock(name="geolocate", side_effect=cycle([(1,1),(2,2)]))
    steps = 10
    
    with patch('requests.get', return_value=Mock(content=mock_map.read())) as mock_get:
        with patch.object(Greengraph,'geolocate',mock_geolocate) as mockgeolocate:
            test_Greengraph = Greengraph('London','Oxford')
            assert test_Greengraph.green_between(steps) == ([106719]*steps)


#test_init()
#test_geolocate_int()
#test_geolocate()
#test_location_sequence()
#test_green_between_int()
#test_green_between()










