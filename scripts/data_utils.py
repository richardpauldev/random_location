from __future__ import annotations

import os
import urllib.request
import zipfile
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

COUNTRIES_URL = (
    "https://naturalearth.s3.amazonaws.com/10m_cultural/ne_10m_admin_0_countries.zip"
)
_ZIP_PATH = DATA_DIR / "ne_10m_admin_0_countries.zip"
_SHAPEFILE = DATA_DIR / "ne_10m_admin_0_countries.shp"


def ensure_countries_dataset() -> str:
    """Download and extract the Natural Earth countries dataset if needed.

    Returns
    -------
    str
        Path to the extracted shapefile.
    """
    if not _SHAPEFILE.exists():
        if not _ZIP_PATH.exists():
            urllib.request.urlretrieve(COUNTRIES_URL, _ZIP_PATH)
        with zipfile.ZipFile(_ZIP_PATH) as zf:
            zf.extractall(DATA_DIR)
    return str(_SHAPEFILE)
