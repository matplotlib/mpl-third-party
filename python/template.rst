{% for section in config %}
    
{{ section.name }}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{{ section.get('intro', '') }}
  
  .. raw:: html

    <div>
    <table>
      {% for package in section.packages %}
      <tr style="vertical-align:top; text-align:center">
        <td style="vertical-align:top; text-align:left; width:10em">
          {% if 'site' in package.badges %} 
            <a href="{{ package.site_protocol}}://{{ package.site }}">{{ package.name }}</a>
          {% else %}
            <a href="http://github.com/{{ package.repo }}">{{ package.name }}</a>
          {% endif %}
        </td>
        <td style="text-align:left; width:30em">  
          {{ package.description }}   
        </td>             
        
        <td>
          <a href="https://github.com/{{ package.user }}/{{ package.name }}">  
          <img style="text-align:left; height:1.4em"  src="_static/badges/github-gray.svg">
            
          </a?>
        </td>

        {% if 'pypi' in package.badges %}
        <td>
          <a href="https://pypi.python.org/pypi/{{ package.pypi_name }}">
            <img style="text-align:left; height:1.4em" src="_static/badges/pip-orange.svg">
          </a>
        </td>
        {% else %}
        <td>-</td>
        {% endif %}
        {% if 'conda' in package.badges %}
        <td>
          <a href="https://anaconda.org/{{ package.conda_channel }}/{{ package.conda_package }}">
          <img style="text-align:left; height:1.4em" src="_static/badges/conda-blue.svg">
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
