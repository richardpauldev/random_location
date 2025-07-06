import random
from pathlib import Path
from typing import Optional

import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon


def random_point_within(poly: Polygon) -> tuple[float, float]:
    minx, miny, maxx, maxy = poly.bounds
    while True:
        p = gpd.points_from_xy([random.uniform(minx, maxx)], [random.uniform(miny, maxy)])[0]
        if poly.contains(p):
            return p.x, p.y


def random_location(shapefile: str, population_field: str = "POP_EST") -> tuple[str, float, float]:
    """Choose a random location weighted by population.

    Parameters
    ----------
    shapefile: str
        Path to a polygon dataset (e.g. Natural Earth countries).
    population_field: str
        Field in the dataset containing population numbers.

    Returns
    -------
    tuple[str, float, float]
        A tuple of the chosen region name, longitude, and latitude.
    """
    gdf = gpd.read_file(shapefile)
    if population_field not in gdf.columns:
        raise ValueError(f"population field '{population_field}' not in dataset")
    populations = gdf[population_field].astype(float)
    weights = populations / populations.sum()
    region = gdf.sample(weights=weights).iloc[0]

    geom = region.geometry
    if isinstance(geom, MultiPolygon):
        # choose one polygon from the multi polygon weighted by area
        areas = [p.area for p in geom.geoms]
        poly = random.choices(list(geom.geoms), weights=areas)[0]
    else:
        poly = geom

    lon, lat = random_point_within(poly)
    return region.get("NAME", region.index), lon, lat

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sample a random location weighted by population")
    parser.add_argument("shapefile", help="Path to shapefile or GeoPackage containing polygons")
    parser.add_argument("population_field", nargs="?", default="POP_EST", help="Column containing population values")
    args = parser.parse_args()

    name, lon, lat = random_location(args.shapefile, args.population_field)
    print(f"{name}: {lon:.6f}, {lat:.6f}")
