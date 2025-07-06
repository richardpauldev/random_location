# Random Location Sampler

This project demonstrates how to select a random geographic point with a probability proportional to population density.

The approach is:

1. Load a dataset of administrative boundaries with associated population figures. Natural Earth `ne_10m_admin_0` is a good starting dataset and includes a `POP_EST` field.
2. Choose a region (e.g. a country) at random with probability proportional to its population.
3. Optionally repeat the process with sub‑regions if more granular data (such as states or provinces) is available.
4. Generate a random coordinate within the selected polygon.

The script `location_sampler.py` implements a basic version of this method using `geopandas` and `shapely`.

```
python -m location_sampler <path-to-shapefile> [population_field]
```

Dependencies are listed in `requirements.txt`.
