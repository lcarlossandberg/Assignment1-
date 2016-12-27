from map import Map
from nose.tools import assert_almost_equal, assert_equal
from mock import Mock, patch
import geopy
import requests
from io import BytesIO
from matplotlib import image as img

def test_init():#have an error which shouldnt happen as its getting mocked, made similar to notes still error
    with patch.object(requests,'get') as mock_get:
        with patch.object(img,'imread') as mock_img:
            default_map=Map(51.0, 0.0)
            mock_get.assert_called_with(
                                        "http://maps.googleapis.com/maps/api/staticmap?",
                                        params={
                                        'sensor':'false',
                                        'zoom':10,
                                        'size':'400x400',
                                        'center':'51.0,0.0',
                                        'style':'feature:all|element:labels|visibility:off',
                                        'maptype': 'satellite'
                                        }
                                        )


#test_init()
