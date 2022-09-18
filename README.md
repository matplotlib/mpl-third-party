# mpl-third-party

List of Matplotlib user-contributed packages.  These are served at
https://matplotlib.org/mpl-third-party/.

To add your package to the list, create a YAML file `your-cool-mpl-package.yml` in the `packages`
directory. The file must have the following fields:

```yml
repo: matplotlib/cmocean
section: colormaps and styles
description: Perceptually uniform colormaps for oceanographic variables.
site: https://matplotlib.org/cmocean # optional, default repo site
keywords: [colormaps, styles] # optional
pypi_name: # optional, default repo name
conda_package: # optional
conda_channel: # optional, default conda-forge
```
Either fork this repo and add the new file there, or navigate into the `packages` directory above
and use the `Add File` button at the top of the page. Then open a pull request with the new file.

Note: The name of the yml file and the name of the repo should ideally match.

The `section` entry should be one of the sections listed in 
[./section_names.yml](https://github.com/matplotlib/mpl-third-party/blob/main/section_names.yml).

### PyPI Classifier
Please add the `Framework :: Matplotlib` PyPI Trove classifier to your package's [setup configuration](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata) to be included in a listing of [Matplotlib related projects](https://pypi.org/search/?c=Framework+%3A%3A+Matplotlib) on PyPI, 

## Development

The list of yml files in `packages/` is parsed by `python/build.py` using `template.rst` and
the result is saved to `docs/source/packages.rst`.  This script is called by `docs/Makefile`
using `make html`.  This runs a `sphinx-build` and makes the page at `build/html/index.html`.

This was heavily based on the nice work at <https://pyviz.org>.
