# Random Location Sampler

This project demonstrates how to select a random geographic point with a probability proportional to population density.

The approach is:

1. Load a dataset of administrative boundaries with associated population figures. The helper in `scripts/data_utils.py` will automatically download the Natural Earth `ne_10m_admin_0` dataset.
2. Choose a region (e.g. a country) at random with probability proportional to its population.
3. Optionally repeat the process with sub‑regions if more granular data (such as states or provinces) is available.
4. Generate a random coordinate within the selected polygon.

The script `location_sampler.py` implements a basic version of this method using `geopandas` and `shapely`. If no shapefile is provided, the Natural Earth countries dataset is downloaded automatically the first time.

```
python -m location_sampler [path-to-shapefile] [population_field]
```

Running without arguments will download the Natural Earth dataset to the `data/` directory and sample from it.

Dependencies are listed in `requirements.txt`.
