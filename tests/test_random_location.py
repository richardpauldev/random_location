from location_sampler import random_location
from scripts.data_utils import ensure_countries_dataset


def test_random_location_builtin():
    # Use an explicit shapefile path
    shapefile = ensure_countries_dataset()
    name, lon, lat = random_location(shapefile, "POP_EST")
    assert isinstance(name, str) and isinstance(lon, float) and isinstance(lat, float)


def test_random_location_download():
    # call without shapefile to trigger dataset download
    name, lon, lat = random_location()
    assert isinstance(name, str) and isinstance(lon, float) and isinstance(lat, float)
