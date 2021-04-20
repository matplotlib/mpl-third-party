# mpl-third-party

List of matplotlib user-contributed packages.  These are served at http://matplotlib.org/mpl-third-party/

To add your package to the list, create a YAML file `your-cool-mpl-package.yml` with the following fields:

```yml
repo: matplotlib/cmocean
site: https://matplotlib.org/cmocean/
keywords:  colormaps
description:  Preceptually uniform colormaps for commonly-used oceanographic variables
pypi_name: # optional, default repo name
conda_package: # optional
conda_channel: # optional, default conda-forge
```
Either fork this repo and add the new file to the `packages` directory, 
or use the `Add File` button above, and then create a PR.

Note: The name of the yml file and the name of the repo should ideally match.

## Development

The list if *yml* files in `packages/` is parsed by `build/build.py` using `template.rst` and
the result is saved to `docs/source/packages.rst`.  This script is called by `docs/Makefile` 
using `make html`.  This runs a `sphinx-build` and makes the page at `build/html/index.html`.  

This was heavily based on the nice work at <https://pyviz.org>.  

