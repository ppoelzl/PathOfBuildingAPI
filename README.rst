Path of Building API
====================

.. image:: https://img.shields.io/maintenance/yes/2021
   :alt: Maintenance
.. image:: https://readthedocs.org/projects/pobapi/badge
   :target: https://pobapi.readthedocs.io
   :alt: Read the Docs - Status
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style - black
.. image:: https://img.shields.io/pypi/pyversions/pobapi
   :target: https://pypi.org/project/pobapi/
   :alt: PyPI - Python Version
.. image:: https://img.shields.io/pypi/v/pobapi
   :target: https://pypi.org/project/pobapi/
   :alt: PyPI
.. image:: https://img.shields.io/pypi/status/pobapi
   :target: https://pypi.org/project/pobapi/
   :alt: PyPI - Status
.. image:: https://img.shields.io/pypi/format/pobapi
   :target: https://pypi.org/project/pobapi/
   :alt: PyPI - Format
.. image:: https://img.shields.io/pypi/l/pobapi
   :target: https://opensource.org/licenses/MIT
   :alt: PyPI - License

Introduction
------------

| Path Of Building API provides a comprehensive toolbox for processing
    `Path of Building <https://github.com/PathOfBuildingCommunity/PathOfBuilding>`_ pastebins.
| It is aimed at community developers:

* looking to add Path of Building functionality to their apps.
* upgrading from existing solutions.

Benefits from using this library:

* Focus on your app's core competences
* Spend your free time on unique features
* Backwards-compatibility as PoB's export format changes
* Tested and secure codebase

Features
--------

* Look up and process:
    * Character stats (DPS, life, etc.)
    * Skill trees
    * Skills, skill groups and links
    * Gear and item sets
    * Path of Building configuration settings
    * Build author's notes
* Exposes all of Path of Building's relevant stats and attributes in a simple and pythonic way.
* Automatically calculates mod values on theorycrafted items.
* Low memory footprint through slots and dynamically generated attributes.

Requirements
------------

* `Python 3.7+ <https://www.python.org/>`_
* `dataslots <https://pypi.org/project/dataslots/>`_
* `lxml <https://pypi.org/project/lxml/>`_
* `requests <https://pypi.org/project/requests/>`_
* `unstdlib <https://pypi.org/project/unstdlib/>`_

Setup Instructions
--------------------

.. code-block:: console

    pip install pobapi

Setup Instructions For Developers
---------------------------------

Setup virtual environment:

.. code-block:: console

    pip install virtualenv
    cd my_project_folder
    virtualenv venv

To activate on Windows:

.. code-block:: console

    \venv\Scripts\activate

To activate on Linux:

.. code-block:: console

    source venv/bin/activate

Setup repository:

.. code-block:: console

    git clone https://github.com/ppoelzl/PathOfBuildingAPI.git
    pip install -r requirements.txt

Basic Usage
-----------

>>> import pobapi
>>> url = "https://pastebin.com/bQRjfedq"
>>> build = pobapi.from_url(url)
>>> print(build.ascendancy_name)
Elementalist
>>> print(build.bandit)
None
>>> print(build.stats.life)
6911
>>> if  build.active_skill.name in ["Blade Vortex", "Vaal Blade Vortex"]:
...     if "Storm Brand" in build.skill_names:
...         print(build.config.brand_attached)
...
True
>>> for item in build.items:
...    if item.name == "Inpulsa's Broken Heart":
...        print(item)
...        break
...
Rarity: Unique
Name: Inpulsa's Broken Heart
Base: Sadist Garb
Quality: 20
Sockets: (('G', 'G', 'G', 'B', 'B', 'B'),)
LevelReq: 68
ItemLvl: 71
+64 to maximum Life
26% increased Damage if you have Shocked an Enemy Recently
33% increased Effect of Shock
Shocked Enemies you Kill Explode, dealing 5% of
their Maximum Life as Lightning Damage which cannot Shock
Unaffected by Shock

Documentation
-------------

Available at `Read the Docs <https://pobapi.readthedocs.io>`_.

Feedback
--------

Please file a `GitHub issue <https://developer.github.com/v3/issues/>`_ in this repository for any feedback you may have.

Contributing
------------

Pull requests are gladly accepted. Check out the `Developer Guide <https://pobapi.readthedocs.io/dev.html>`_.

Roadmap
-----

* Support corruptions
* Support enchantments

License
-------

`MIT <https://mit-license.org/>`_
