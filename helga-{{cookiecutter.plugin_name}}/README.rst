helga-{{ cookiecutter.plugin_name }}
==============

.. image:: https://badge.fury.io/py/helga-{{ cookiecutter.plugin_name }}.png
    :target: https://badge.fury.io/py/helga-{{ cookiecutter.plugin_name }}

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/helga-{{ cookiecutter.plugin_name }}.png?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/helga-{{ cookiecutter.plugin_name }}

{{ cookiecutter.plugin_description }}

Installation
------------

Install via pip::

    pip install helga-{{ cookiecutter.plugin_name }}

And add to settings!

Usage
-----

    !{{ cookiecutter.plugin_name }} help

Development
-----------

Install all the testing requirements::

    pip install -r requirements_test.txt

Run tox to ensure everything works::

    make test

You may also invoke `tox` directly if you wish.

Release
-------

To publish your plugin to pypi, sdist and wheels are (registered,) created and uploaded with::

    make release

License
-------

Copyright (c) {% now 'local', '%Y' %} {{ cookiecutter.author_name }}

See LICENSE for details
