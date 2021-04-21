{% for section in config %}

{{ section.name }}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{{ section.get('intro', '') }}

  .. raw:: html

    <div>
    <table style="vertical-align:top; text-align:left">
      <colgroup>
        <col style="width: 10em">
        <col>
      </colgroup>
      {%- for package in section.packages %}
      <tr>
        <td>
          {%- if 'site' in package.badges %}
          <a href="{{ package.site_protocol }}://{{ package.site }}">{{ package.name }}</a>
          {%- else %}
          <a href="http://github.com/{{ package.repo }}">{{ package.name }}</a>
          {%- endif %}
        </td>
        <td align="left">
          {{ package.description }}
        </td>
      </tr>
      <tr>
        <td/>
        <td>
          <a href="https://github.com/{{ package.user }}/{{ package.name }}">
            <img src="https://img.shields.io/github/stars/{{ package.user }}/{{ package.name }}.svg?style=social">
          </a>
          {%- if 'pypi' in package.badges %}
          <a href="https://pypi.python.org/pypi/{{ package.pypi_name }}">
            <img src="https://img.shields.io/pypi/v/{{ package.pypi_name }}.svg?label?logoWidth=100">
          </a>
          {%- endif %}
          {%- if 'conda' in package.badges %}
          <a href="https://anaconda.org/{{ package.conda_channel }}/{{ package.conda_package }}">
            <img src="https://img.shields.io/conda/vn/{{ package.conda_channel }}/{{ package.conda_package }}.svg?style=flat?logoWidth=40">
          </a>
          {%- endif %}
        </td>
      </tr>
      {%- endfor %}
    </table>
    {%- endfor %}
    </div>
