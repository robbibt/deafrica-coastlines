#!/usr/bin/env python3

import os
from setuptools import find_packages, setup

# Where are we?
IS_SANDBOX = "sandbox" in os.getenv("JUPYTER_IMAGE", default="")

# What packages are required for this module to be executed?
REQUIRED = [
    "aiohttp",
    "affine",
    "botocore",
    "click",
    "datacube",
    "dea_tools",
    "fiona",
    "geopandas",
    "geopy",
    "matplotlib",
    "mock",
    "numpy",
    "odc_ui",
    "otps",
    "pandas",
    "pyproj",
    "pytz",
    "rasterio",
    "rasterstats",
    "Rtree",
    "setuptools-scm",
    "scikit_image",
    "scikit_learn",
    "scipy",
    "shapely",
    "tqdm",
    "xarray",
]

# Package metadata
NAME = "deafrica_coastlines"
DESCRIPTION = "Tools for running Digital Earth Africa Coastlines"
URL = "https://github.com/digitalearthafrica/deafrica-coastlines"
EMAIL = "Robbi.BishopTaylor@ga.gov.au"
AUTHOR = "Robbi Bishop-Taylor"
REQUIRES_PYTHON = ">=3.8.0"

# Setup kwargs
setup_kwargs = {
    "name": NAME,
    "description": DESCRIPTION,
    "long_description": DESCRIPTION,
    "long_description_content_type": "text/markdown",
    "author": AUTHOR,
    "author_email": EMAIL,
    "python_requires": REQUIRES_PYTHON,
    "url": URL,
    "install_requires": REQUIRED if not IS_SANDBOX else ["mock", "dea_tools"],
    "packages": find_packages(),
    "include_package_data": True,
    "license": "Apache License 2.0",
    "entry_points": {
        "console_scripts": [
            "deafricacoastlines-raster = deafrica_coastlines.raster:generate_rasters",
            "deafricacoastlines-vector = deafrica_coastlines.vector:generate_vectors",
            "deafricacoastlines-continental = deafrica_coastlines.continental:continental_layers",
        ]
    },
}

setup(**setup_kwargs)
