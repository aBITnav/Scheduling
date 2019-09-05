import googlemaps
from datetime import datetime, timedelta
import time
import json

API_key = ""

def distance_calc(sources, destinations):
    """
    :param sources: ['12.916936,77.516220' ]
    :param destinations: ['12.916786,77.605472']
    """

    gmaps = googlemaps.Client(key=API_key)

    res = gmaps.distance_matrix(
            sources,
            destinations, 
            mode="walking",
            departure_time=datetime.now() + timedelta(hours=12),
            units="metric"
        )
    assert objects.get(res, 'status') == 'OK'
    return objects.get(res, 'rows.0.elements')
