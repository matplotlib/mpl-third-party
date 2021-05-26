.. raw:: html

  <div>
  <table>
  {% for section in config %}
    <tr>
      <td colspan=5 style="height:4em; vertical-align:center">
        {% with section_id = section.name | lower | replace(" ", "-") %}
        <h3 id="{{ section_id }}">
          {{ section.name }}
          <a class="headerlink" href="#{{ section_id }}" title="Permalink to this headline">¶</a>
        </h3>
        {% endwith %}
      </td>
    </tr>

      {% for package in section.packages %}
      <tr>
        
        <td style="text-align:left; vertical-align:top;">
          <a href="https://github.com/{{ package.user }}/{{ package.name }}">  
            <img style="text-align:left; height:1.4em; max-width: none;"  src="_static/badges/github-gray.svg">
          </a>
        </td>

      {% if 'pypi' in package.badges %}
        <td style="text-align:left; vertical-align:top;">
          <a href="https://pypi.python.org/pypi/{{ package.pypi_name }}">
            <img style="text-align:left; height:1.4em; max-width: none;" src="_static/badges/pip-orange.svg">
          </a>
        </td>
        {% else %}
        <td style="text-align:center; style="vertical-align:top;">
          <img style="text-align:left; height:1.4em; max-width: none;" src="_static/badges/pip-empty.svg">
        </td>
        {% endif %}
      {% if 'conda' in package.badges %}
        <td style="text-align:left; vertical-align:top;">
          <a href="https://anaconda.org/{{ package.conda_channel }}/{{ package.conda_package }}">
          <img style="text-align:left; height:1.4em; max-width: none;" src="_static/badges/conda-blue.svg">
          </a>
        </td>
      {% else %}
        <td style="text-align:left;vertical-align:top; ">
          <img style="text-align:left; height:1.4em; max-width: none;" src="_static/badges/conda-empty.svg">
        </td>        
      {% endif %}  

      <td style="vertical-align:top; text-align:left;cellpadding:0.3em">
      {% if 'site' in package.badges %} 
        <a href="{{ package.site_protocol}}://{{ package.site }}">{{ package.name }}</a>
      {% else %}
        <a href="http://github.com/{{ package.repo }}">{{ package.name }}</a>
      {% endif %}
      </td>
      <td style="text-align:left;vertical-align:top;cellpadding:0.3em">  
        {{ package.description }}   
      </td>             
      

      </tr>
      {% endfor %}
    {% endfor %}
    </table>
    </div>
