#!/usr/bin/env python
"""
Run this script at the beginning of each month to build new conda downloads badges
from the previous month.
"""

import datetime
from pathlib import Path
import warnings

import colorcet as cc
import intake
import numpy as np
import requests
from yaml import safe_load


here = Path(__file__).parent.resolve()
cache_path = here.parent / 'doc/_static/cache'
cat = intake.open_catalog(
    'https://raw.githubusercontent.com/ContinuumIO/anaconda-package-data/'
    'master/catalog/anaconda_package_data.yaml')

colors = cc.palette_n.rainbow[-20:80:-1]
top_of_colormap = 1e6
step = len(colors) / np.log10(top_of_colormap)

today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)
try:
    monthly = cat.anaconda_package_data_by_month(
        year=last_month.year, month=last_month.month,
        columns=['pkg_name', 'counts']).to_dask()
except Exception:
    # if the last month isn't available, get the month before
    month_before = last_month.replace(day=1) - datetime.timedelta(days=1)
    monthly = cat.anaconda_package_data_by_month(
        year=month_before.year, month=month_before.month,
        columns=['pkg_name', 'counts']).to_dask()
per_package_downloads = monthly.groupby('pkg_name').sum().compute()

cache_path.mkdir(exist_ok=True)


def get_conda_badge(conda_package):
    conda_package = conda_package.lower()
    if conda_package in per_package_downloads.index:
        downloads = per_package_downloads.counts.loc[conda_package]
    else:
        downloads = 0

    if downloads == 0:
        color_index = 0
    elif downloads > top_of_colormap:
        color_index = -1
    else:
        color_index = int(np.log10(downloads) * step)
    color = colors[color_index][1:]

    if downloads > 1e6:
        downloads = '{}M'.format(int(downloads/1e6))
    elif downloads > 1e3:
        downloads = '{}k'.format(int(downloads/1e3))
    else:
        downloads = int(downloads)

    return f"https://img.shields.io/badge/conda-{downloads}/month-{color}.svg"


with (here / 'tools.yml').open() as f:
    config = safe_load(f)

for section in config:
    print(f"Building conda downloads badge for: {section['name']}")
    for package in section['packages']:
        try:
            package['user'], package['repo_name'] = package['repo'].split('/')
        except ValueError:
            warnings.warn(f'Package.repo is not in correct format: {package}')
            continue
        url = get_conda_badge(package.get('conda_package', package['repo_name']))
        rendered_url = url
        r = requests.get(rendered_url)
        badge = (cache_path / f"{package['repo_name']}_conda_downloads_badge.svg")
        badge.write_bytes(r.content)
