{% for section in config %}
    
{{ section.name }}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{{ section.get('intro', '') }}
  
  .. raw:: html

    <div>
    <table>
      <tr style="text-align:center">
        <th style="width:10em">Name</th>
        <th style="width:30em;">Description</th>
        <th style="width:6em; text-align:center">GitHub</th>
        <th style="width:6em; text-align:center">PyPI</th>
        <th style="text-align:center; width:9em">Conda</th>
      </tr>
      {% for package in section.packages %}
      <tr style="vertical-align:top; text-align:center">
        <td style="vertical-align:top; text-align:left">
          {% if 'site' in package.badges %} 
            <a href="{{ package.site_protocol}}://{{ package.site }}">{{ package.name }}</a>
          {% else %}
            <a href="http://github.com/{{ package.repo }}">{{ package.name }}</a>
          {% endif %}
        </td>
        <td align='left'>  
          {{ package.description }}   
        </td>             
        
        <td>
          <a href = "https://github.com/{{ package.user }}/{{ package.name }}">
            <img src="https://img.shields.io/github/stars/{{ package.user }}/{{ package.name }}.svg?style=social">
          </a?>
        </td>

        {% if 'pypi' in package.badges %}
        <td >
          <a href="https://pypi.python.org/pypi/{{ package.pypi_name }}">
            <img src="https://img.shields.io/pypi/v/{{ package.pypi_name }}.svg?label?logoWidth=100">
          </a>
        </td>
        {% else %}
        <td>-</td>
        {% endif %}
        {% if 'conda' in package.badges %}
        <td>
          <a href="https://anaconda.org/{{ package.conda_channel }}/{{ package.conda_package }}">
          <img src="https://img.shields.io/conda/vn/{{ package.conda_channel }}/{{ package.conda_package }}.svg?style=flat?logoWidth=40">
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
