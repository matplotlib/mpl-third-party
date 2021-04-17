{% for section in config %}
    
{{ section.name }}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{{ section.get('intro', '') }}
  
  .. raw:: html

    <div>
    <table>
      <tr style="text-align:center">
        <th style="width:10em">Name</th>
        <th>Description</th>
        <th style="width:6em; text-align:center">Website</th>
        <th style="width:4em; text-align:center">PyPi</th>
        <th style="text-align:center; width:6em">Conda</th>
      </tr>
      {% for package in section.packages %}
      <tr style="vertical-align:top; text-align:center">
        <td style="vertical-align:top; text-align:left">
          <a href="http://github.com/{{ package.repo }}">{{ package.name }}</a>
        </td>
        <td align='left'>  {{ package.description }}   </td>             
        {% if 'site' in package.badges %}
        <td>
          <a href="{{ package.site_protocol}}://{{ package.site }}">
            <img src="https://img.shields.io/website-up-down-green-red/{{ package.site_protocol}}/{{ package.site }}.svg">
          </a>
        </td>
        {% elif 'rtd' in package.badges %}
        <td>
          <a href="https://{{ package.rtd_name }}.readthedocs.io">
            <img src="https://readthedocs.org/projects/{{ package.rtd_name }}/badge/?version=latest">
          </a>
        </td>
        {% else %}
        <td><a href="http://github.com/{{ package.repo }}">github</a></td>
        {% endif %}
        {% if 'pypi' in package.badges %}
        <td >
          <a href="https://pypi.python.org/pypi/{{ package.pypi_name }}">
            <img src="https://img.shields.io/pypi/v/{{ package.pypi_name }}.svg?label">
          </a>
        </td>
        {% else %}
        <td>-</td>
        {% endif %}
        {% if 'conda' in package.badges %}
        <td>
          <a href="https://anaconda.org/{{ package.conda_channel }}/{{ package.conda_package }}">
          <img src="https://img.shields.io/conda/vn/{{ package.conda_channel }}/{{ package.conda_package }}.svg?style=flat">
          </a>
        </td>
        {% else %}
        <td>-</td>        
        {% endif %}  
      </tr>
      {% endfor %}
    </table>
    {% endfor %}
    </div>
