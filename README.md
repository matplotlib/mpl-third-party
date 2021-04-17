# mpl-user-contrib
List of matplotlib user-contributed packages.  These are served at <http://matplotlib.org/mpl-user-contrib.html>

To add your package to the list create a YAML file `your-cool-mpl-package.yml` with the following fields:

```yml
repo: matplotlib/cmocean
site: https://matplotlib.org/cmocean/
keywords:  colormaps
description:  Preceptually uniform colormaps for commonly-used oceanographic variables
```

Other descriptors can be `pypi_name`, `conda_package`, and `conda_channel`, 
`pypi_name` will automatically fill with the repo name if `pypi_name` is not supplied.  

Either fork this repo and add the new file to the `packages` directory,
or use the `Add File` button above, and then create a PR.

Note that the name of the yml and the name of the repo should ideally match.



