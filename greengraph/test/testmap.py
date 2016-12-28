from map import Map
from nose.tools import assert_almost_equal, assert_equal
from mock import Mock, patch
import geopy
import requests
from io import BytesIO
from matplotlib import image as img
import os
import numpy as np

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

def test_green():
    mock_map = open(os.path.join(os.path.dirname(__file__),'fixtures','London.png'),'rb')
    mock_pixel = np.load(os.path.join(os.path.dirname(__file__),'fixtures','LondonData.npy'))
    threshold = 1.1
    with patch('requests.get', return_value=Mock(content=mock_map.read())) as mock_get:
         test_Map = Map(51.5074,-0.1278)
         assert (test_Map.green(threshold) == mock_pixel).all() == True


def test_count_green():
    mock_map = open(os.path.join(os.path.dirname(__file__),'fixtures','London.png'),'rb')
    threshold = 1.1
    with patch('requests.get', return_value=Mock(content=mock_map.read())) as mock_get:
        test_Map = Map(51.5074,-0.1278)
        assert test_Map.count_green(threshold) == 106719

#test_init()
#test_green()
#test_count_green()

#show_green was not tested as it was removed for the code due to not being used



