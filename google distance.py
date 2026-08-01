"""
Module: google distance
Description: Fetches walking distance matrices using the Google Maps API.
"""
import googlemaps
from datetime import datetime, timedelta
import time
import json
from pydash import objects

def distance_calc(api_key, sources, destinations):
    """
    Fetches the distance matrix from the Google Maps API.
    :param api_key: str - Google Maps API key
    :param sources: list - e.g. ['12.916936,77.516220']
    :param destinations: list - e.g. ['12.916786,77.605472']
    """
    gmaps = googlemaps.Client(key=api_key)

    res = gmaps.distance_matrix(
            sources,
            destinations, 
            mode="walking",
            departure_time=datetime.now() + timedelta(hours=12),
            units="metric"
        )
    assert objects.get(res, 'status') == 'OK'
    return objects.get(res, 'rows.0.elements')

def main():
    """Main execution block."""
    api_key = ""
    # Example usage:
    # sources = ['12.916936,77.516220']
    # destinations = ['12.916786,77.605472']
    # print(distance_calc(api_key, sources, destinations))

if __name__ == '__main__':
    main()
